import { Session } from '../api/p0-contract.types';
import { AccessTokenStore } from './access-token-store';

export class RefreshTerminalError extends Error {
  constructor(readonly code: 'refresh_invalid' | 'refresh_reused') {
    super(code);
    this.name = 'RefreshTerminalError';
  }
}

export interface RefreshTransport {
  refresh(signal?: AbortSignal): Promise<Session>;
}

export class AuthRefreshCoordinator {
  private inFlight: Promise<Session> | undefined;

  constructor(
    private readonly transport: RefreshTransport,
    private readonly tokens: AccessTokenStore,
  ) {}

  refresh(signal?: AbortSignal): Promise<Session> {
    if (!this.inFlight) {
      this.inFlight = this.transport
        .refresh(signal)
        .then((session) => {
          this.tokens.set(session);
          return session;
        })
        .catch((error: unknown) => {
          if (error instanceof RefreshTerminalError) {
            this.tokens.clear();
          }
          throw error;
        })
        .finally(() => {
          this.inFlight = undefined;
        });
    }
    return this.inFlight;
  }
}
