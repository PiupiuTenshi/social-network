export type ApiFailureKind = 'auth' | 'precondition' | 'rate-limit' | 'server' | 'network' | 'api';

export interface ProblemDetails {
  readonly code?: string;
  readonly message: string;
  readonly correlationId?: string;
  readonly status: number;
  readonly retryAfterSeconds?: number;
}

export class ApiFailure extends Error {
  constructor(
    readonly kind: ApiFailureKind,
    readonly problem: ProblemDetails,
  ) {
    super(problem.message);
    this.name = 'ApiFailure';
  }
}

export async function failureFrom(response: Response): Promise<ApiFailure> {
  const retryAfter = response.headers.get('retry-after');
  const retryAfterSeconds = retryAfter && /^\d+$/.test(retryAfter) ? Number(retryAfter) : undefined;
  let body: unknown;
  try {
    body = await response.json();
  } catch {
    body = undefined;
  }
  const record = body as
    | {
        error?: { code?: unknown; message?: unknown; correlationId?: unknown };
        title?: unknown;
        detail?: unknown;
      }
    | undefined;
  const error = record?.error;
  const code = typeof error?.code === 'string' ? error.code : undefined;
  const message =
    typeof error?.message === 'string'
      ? error.message
      : typeof record?.detail === 'string'
        ? record.detail
        : typeof record?.title === 'string'
          ? record.title
          : `HTTP ${response.status}`;
  const correlationId = typeof error?.correlationId === 'string' ? error.correlationId : undefined;
  const kind: ApiFailureKind =
    response.status === 401 || response.status === 403
      ? 'auth'
      : response.status === 412
        ? 'precondition'
        : response.status === 429
          ? 'rate-limit'
          : response.status >= 500
            ? 'server'
            : 'api';
  return new ApiFailure(kind, {
    code,
    message,
    correlationId,
    status: response.status,
    retryAfterSeconds,
  });
}
