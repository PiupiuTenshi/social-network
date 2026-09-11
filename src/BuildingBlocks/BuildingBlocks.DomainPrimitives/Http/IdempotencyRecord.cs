namespace BuildingBlocks.DomainPrimitives.Http;

public sealed record IdempotencyRecord(string Key, string RequestHash, int StatusCode, string ResponseBody, DateTimeOffset ExpiresAt);
