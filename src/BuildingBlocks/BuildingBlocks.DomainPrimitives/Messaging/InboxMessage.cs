namespace BuildingBlocks.DomainPrimitives.Messaging;

/// <summary>Idempotency boundary: a duplicate event id has no second side effect.</summary>
public sealed record InboxMessage(Guid EventId, DateTimeOffset ProcessedAt);
