import { Session } from '../api/p0-contract.types';

export interface AccessSession {
  readonly accessToken: string;
  readonly expiresAt: string;
}

export class AccessTokenStore {
  private session: AccessSession | null = null;

  set(session: Session): void {
    this.session = { accessToken: session.accessToken, expiresAt: session.expiresAt };
  }

  clear(): void {
    this.session = null;
  }

  get accessToken(): string | null {
    return this.session?.accessToken ?? null;
  }

  get current(): AccessSession | null {
    return this.session;
  }
}
