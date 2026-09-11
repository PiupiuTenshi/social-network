namespace Account.Infrastructure.Persistence;

public sealed class OutboxRecord
{
    public Guid EventId { get; set; }
    public required string EventType { get; set; }
    public int EventVersion { get; set; }
    public DateTimeOffset OccurredAt { get; set; }
    public required string CorrelationId { get; set; }
    public Guid AggregateId { get; set; }
    public long AggregateVersion { get; set; }
    public required string Payload { get; set; }
    public DateTimeOffset? PublishedAt { get; set; }
    public int Attempts { get; set; }
}

public sealed class InboxRecord
{
    public Guid EventId { get; set; }
    public DateTimeOffset ProcessedAt { get; set; }
}

public sealed class IdempotencyRecord
{
    public required string Key { get; set; }
    public required string RequestHash { get; set; }
    public int StatusCode { get; set; }
    public required string ResponseBody { get; set; }
    public DateTimeOffset ExpiresAt { get; set; }
}
