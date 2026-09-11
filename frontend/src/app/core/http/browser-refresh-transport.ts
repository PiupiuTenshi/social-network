import { Session } from '../api/p0-contract.types';
import { RefreshTerminalError, RefreshTransport } from '../auth/auth-refresh-coordinator';
import { ApiFailure, failureFrom } from './problem-details';

export interface FetchLike {
  (input: RequestInfo | URL, init?: RequestInit): Promise<Response>;
}

export function apiUrl(path: string, baseUrl: string): URL {
  const normalizedBaseUrl = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
  return new URL(path.replace(/^\/+/, ''), normalizedBaseUrl);
}

export class BrowserRefreshTransport implements RefreshTransport {
  constructor(
    private readonly fetcher: FetchLike,
    private readonly baseUrl: string,
  ) {}

  async refresh(signal?: AbortSignal): Promise<Session> {
    let response: Response;
    try {
      response = await this.fetcher(apiUrl('auth/refresh', this.baseUrl), {
        method: 'POST',
        credentials: 'include',
        signal,
      });
    } catch (error) {
      throw error;
    }
    if (response.ok) return response.json() as Promise<Session>;
    const failure = await failureFrom(response);
    if (failure.problem.code === 'refresh_invalid' || failure.problem.code === 'refresh_reused') {
      throw new RefreshTerminalError(failure.problem.code);
    }
    throw failure;
  }
}

export class RequestLifecycle {
  private readonly active = new Map<string, AbortController>();

  begin(
    key: string,
    parent?: AbortSignal,
  ): {
    readonly signal: AbortSignal;
    readonly isCurrent: () => boolean;
    readonly complete: () => void;
  } {
    this.active.get(key)?.abort();
    const controller = new AbortController();
    const forwardAbort = () => controller.abort();
    parent?.addEventListener('abort', forwardAbort, { once: true });
    this.active.set(key, controller);
    return {
      signal: controller.signal,
      isCurrent: () => this.active.get(key) === controller,
      complete: () => {
        parent?.removeEventListener('abort', forwardAbort);
        if (this.active.get(key) === controller) this.active.delete(key);
      },
    };
  }
}

export class StaleResponseError extends Error {
  constructor() {
    super('stale_response');
    this.name = 'StaleResponseError';
  }
}
