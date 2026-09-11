namespace BuildingBlocks.DomainPrimitives.Messaging;

/// <summary>Immutable, versioned envelope persisted by Outbox and Inbox.</summary>
public sealed record EventEnvelope(
    Guid EventId,
    string EventType,
    int EventVersion,
    DateTimeOffset OccurredAt,
    string Producer,
    string CorrelationId,
    Guid AggregateId,
    long AggregateVersion,
    string Payload);
