import { AccessTokenStore } from '../src/app/core/auth/access-token-store';
import {
  AuthRefreshCoordinator,
  RefreshTerminalError,
} from '../src/app/core/auth/auth-refresh-coordinator';
import { P0ApiClient } from '../src/app/core/http/p0-api-client';
import {
  BrowserRefreshTransport,
  StaleResponseError,
} from '../src/app/core/http/browser-refresh-transport';
import { ApiFailure } from '../src/app/core/http/problem-details';
import { SignalRRealtimeAdapter } from '../src/app/core/realtime/realtime-adapter';

function equal(actual: unknown, expected: unknown, message: string): void {
  if (actual !== expected)
    throw new Error(`${message}: expected ${String(expected)}, got ${String(actual)}`);
}
function ok(value: unknown, message: string): void {
  if (!value) throw new Error(message);
}
function json(body: unknown, status = 200, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', ...headers },
  });
}

async function testSingleFlightAndRetry(): Promise<void> {
  const tokens = new AccessTokenStore();
  let refreshCalls = 0;
  let apiCalls = 0;
  const fetcher = async (input: RequestInfo | URL, init?: RequestInit): Promise<Response> => {
    const path = new URL(input.toString()).pathname;
    if (path.endsWith('/auth/refresh')) {
      refreshCalls += 1;
      await Promise.resolve();
      return json({ accessToken: 'test-value', expiresAt: '2030-01-01T00:00:00Z' });
    }
    equal(path, '/api/v1/write', 'API path retains configured version prefix');
    apiCalls += 1;
    if (apiCalls === 1)
      return json({ error: { code: 'expired', message: 'expired', correlationId: 'c1' } }, 401);
    equal(
      new Headers(init?.headers).get('idempotency-key'),
      'request-key',
      'retry retains Idempotency-Key',
    );
    equal(init?.body, '{"value":1}', 'retry retains request body');
    equal(
      new Headers(init?.headers).get('authorization'),
      'Bearer test-value',
      'retry uses refreshed token',
    );
    return json({ ok: true });
  };
  const coordinator = new AuthRefreshCoordinator(
    new BrowserRefreshTransport(fetcher, 'https://api.example.test/api/v1'),
    tokens,
  );
  await Promise.all([coordinator.refresh(), coordinator.refresh(), coordinator.refresh()]);
  equal(refreshCalls, 1, 'concurrent refresh must be single-flight');
  const client = new P0ApiClient(fetcher, 'https://api.example.test/api/v1', tokens, coordinator);
  const result = await client.requestJson<{ ok: boolean }>({
    path: '/write',
    method: 'POST',
    body: '{"value":1}',
    headers: { 'Idempotency-Key': 'request-key' },
  });
  equal(result.ok, true, 'retry returns response');
  equal(refreshCalls, 2, '401 invokes one additional refresh');
}

async function testTerminalAndFailures(): Promise<void> {
  const tokens = new AccessTokenStore();
  tokens.set({ accessToken: 'test-value', expiresAt: '2030-01-01T00:00:00Z' });
  const terminal = new AuthRefreshCoordinator(
    new BrowserRefreshTransport(
      async () =>
        json({ error: { code: 'refresh_reused', message: 'reused', correlationId: 'c2' } }, 401),
      'https://api.example.test',
    ),
    tokens,
  );
  let thrown: unknown;
  try {
    await terminal.refresh();
  } catch (error) {
    thrown = error;
  }
  ok(thrown instanceof RefreshTerminalError, 'refresh reuse must be terminal');
  equal(tokens.accessToken, null, 'terminal refresh clears memory token');
  const failureClient = new P0ApiClient(
    async () => json({ error: { code: 'stale', message: 'stale', correlationId: 'c3' } }, 412),
    'https://api.example.test',
    tokens,
    terminal,
  );
  try {
    await failureClient.requestJson({ path: '/settings' });
  } catch (error) {
    thrown = error;
  }
  ok(
    thrown instanceof ApiFailure && thrown.kind === 'precondition',
    '412 maps to precondition failure',
  );
}

async function testCancellationAndRealtime(): Promise<void> {
  const tokens = new AccessTokenStore();
  const coordinator = new AuthRefreshCoordinator(
    {
      refresh: async () => {
        throw new Error('unused');
      },
    },
    tokens,
  );
  let firstAborted = false;
  const client = new P0ApiClient(
    (_input, init) =>
      new Promise<Response>((resolveResponse, reject) => {
        init?.signal?.addEventListener(
          'abort',
          () => {
            firstAborted = true;
            reject(new DOMException('aborted', 'AbortError'));
          },
          { once: true },
        );
        setTimeout(() => resolveResponse(json({ ok: true })), 5);
      }),
    'https://api.example.test',
    tokens,
    coordinator,
  );
  const first = client.requestJson({ path: '/feed', resourceKey: 'feed' }).catch(() => undefined);
  const second = client.requestJson<{ ok: boolean }>({ path: '/feed', resourceKey: 'feed' });
  await first;
  equal((await second).ok, true, 'latest response succeeds');
  equal(firstAborted, true, 'new keyed request aborts obsolete request');
  let starts = 0,
    stops = 0,
    received: unknown;
  const adapter = new SignalRRealtimeAdapter({
    create: () => ({
      start: async () => {
        starts += 1;
      },
      stop: async () => {
        stops += 1;
      },
      on: (_event, listener) => {
        listener({ delivered: true });
        return () => undefined;
      },
    }),
  });
  await adapter.connect();
  const unsubscribe = adapter.subscribe('message', (payload) => {
    received = payload;
  });
  unsubscribe();
  await adapter.disconnect();
  equal(starts, 1, 'realtime adapter starts one SignalR connection');
  equal(stops, 1, 'realtime adapter stops connection');
  ok((received as { delivered?: boolean }).delivered, 'realtime listener receives payload');
}

async function main(): Promise<void> {
  await testSingleFlightAndRetry();
  await testTerminalAndFailures();
  await testCancellationAndRealtime();
  console.log(
    'Adapter harness passed: refresh, retry, failure, cancellation and realtime lifecycle.',
  );
}

void main().catch((error: unknown) => {
  throw error;
});
