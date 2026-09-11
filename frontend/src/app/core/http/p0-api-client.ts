import { AccessTokenStore } from '../auth/access-token-store';
import { AuthRefreshCoordinator, RefreshTerminalError } from '../auth/auth-refresh-coordinator';
import { ApiFailure, failureFrom } from './problem-details';
import {
  apiUrl,
  FetchLike,
  RequestLifecycle,
  StaleResponseError,
} from './browser-refresh-transport';

export interface ApiRequest {
  readonly path: string;
  readonly method?: string;
  readonly headers?: Readonly<Record<string, string>>;
  readonly body?: BodyInit | null;
  readonly signal?: AbortSignal;
  readonly resourceKey?: string;
}

export class P0ApiClient {
  private readonly lifecycle = new RequestLifecycle();

  constructor(
    private readonly fetcher: FetchLike,
    private readonly baseUrl: string,
    private readonly tokens: AccessTokenStore,
    private readonly refresh: AuthRefreshCoordinator,
  ) {}

  async requestJson<T>(request: ApiRequest): Promise<T> {
    return this.send<T>(request, true);
  }

  private async send<T>(request: ApiRequest, canRefresh: boolean): Promise<T> {
    const lifecycle = request.resourceKey
      ? this.lifecycle.begin(request.resourceKey, request.signal)
      : undefined;
    const headers = new Headers(request.headers);
    const accessToken = this.tokens.accessToken;
    if (accessToken) headers.set('Authorization', `Bearer ${accessToken}`);
    try {
      const response = await this.fetcher(apiUrl(request.path, this.baseUrl), {
        method: request.method ?? 'GET',
        headers,
        body: request.body,
        signal: lifecycle?.signal ?? request.signal,
        credentials: 'include',
      });
      const isRefreshRequest = request.path.replace(/^\/+/, '') === 'auth/refresh';
      if (response.status === 401 && canRefresh && !isRefreshRequest) {
        await this.refresh.refresh(lifecycle?.signal ?? request.signal);
        return this.send<T>(request, false);
      }
      if (!response.ok) throw await failureFrom(response);
      if (lifecycle && !lifecycle.isCurrent()) throw new StaleResponseError();
      return response.json() as Promise<T>;
    } catch (error) {
      if (error instanceof RefreshTerminalError) throw error;
      if (error instanceof ApiFailure) throw error;
      throw error;
    } finally {
      lifecycle?.complete();
    }
  }
}
