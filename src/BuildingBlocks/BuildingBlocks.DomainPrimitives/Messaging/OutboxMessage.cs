namespace BuildingBlocks.DomainPrimitives.Messaging;

/// <summary>Persisted with the owning aggregate; publication is always asynchronous.</summary>
public sealed class OutboxMessage(EventEnvelope envelope)
{
    public EventEnvelope Envelope { get; } = envelope;
    public DateTimeOffset? PublishedAt { get; private set; }
    public int Attempts { get; private set; }

    public void MarkPublished(DateTimeOffset publishedAt) => PublishedAt ??= publishedAt;
    public void RecordAttempt() => Attempts++;
}
