export interface RealtimeConnection {
  start(signal?: AbortSignal): Promise<void>;
  stop(): Promise<void>;
  on(event: string, listener: (payload: unknown) => void): () => void;
}

export interface SignalRConnectionFactory {
  create(): RealtimeConnection;
}

export class SignalRRealtimeAdapter {
  private connection: RealtimeConnection | undefined;

  constructor(private readonly factory: SignalRConnectionFactory) {}

  async connect(signal?: AbortSignal): Promise<void> {
    if (!this.connection) this.connection = this.factory.create();
    await this.connection.start(signal);
  }

  subscribe(event: string, listener: (payload: unknown) => void): () => void {
    if (!this.connection) throw new Error('realtime_not_connected');
    return this.connection.on(event, listener);
  }

  async disconnect(): Promise<void> {
    const connection = this.connection;
    this.connection = undefined;
    if (connection) await connection.stop();
  }
}

export interface LiveKitAdapter {
  connectRoom(): Promise<void>;
  disconnectRoom(): Promise<void>;
}
