using Confluent.Kafka;
using Microsoft.EntityFrameworkCore;
using Account.Infrastructure.Persistence;
using BuildingBlocks.DomainPrimitives.Observability;

namespace Account.Infrastructure.Messaging;

public sealed class KafkaOutboxPublisher(AccountDbContext db, IProducer<string, string> producer)
{
    public async Task<int> PublishPendingAsync(string topic, CancellationToken cancellationToken)
    {
        var pending = await db.Outbox.Where(message => message.PublishedAt == null).OrderBy(message => message.OccurredAt).Take(100).ToListAsync(cancellationToken);
        foreach (var message in pending)
        {
            using var activity = PlatformMetrics.ActivitySource.StartActivity("outbox.publish");
            message.Attempts++;
            await producer.ProduceAsync(topic, new Message<string, string> { Key = message.AggregateId.ToString(), Value = message.Payload, Headers = new Headers { { "eventId", System.Text.Encoding.UTF8.GetBytes(message.EventId.ToString()) }, { "correlationId", System.Text.Encoding.UTF8.GetBytes(message.CorrelationId) } } }, cancellationToken);
            message.PublishedAt = DateTimeOffset.UtcNow;
            PlatformMetrics.OutboxPublished.Add(1);
            PlatformMetrics.OutboxAgeSeconds.Record((DateTimeOffset.UtcNow - message.OccurredAt).TotalSeconds);
        }
        await db.SaveChangesAsync(cancellationToken);
        return pending.Count;
    }
}
