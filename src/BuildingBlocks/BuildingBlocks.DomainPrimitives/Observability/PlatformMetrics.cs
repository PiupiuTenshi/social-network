using System.Diagnostics;
using System.Diagnostics.Metrics;

namespace BuildingBlocks.DomainPrimitives.Observability;

public static class PlatformMetrics
{
    public static readonly ActivitySource ActivitySource = new("TwightLight.Platform");
    private static readonly Meter Meter = new("TwightLight.Platform");
    public static readonly Counter<long> OutboxPublished = Meter.CreateCounter<long>("outbox_published_total");
    public static readonly Counter<long> InboxDuplicate = Meter.CreateCounter<long>("inbox_duplicate_total");
    public static readonly Histogram<double> OutboxAgeSeconds = Meter.CreateHistogram<double>("outbox_age_seconds");
    public static readonly Counter<long> DlqMessages = Meter.CreateCounter<long>("dlq_messages_total");
    public static readonly Histogram<double> ConsumerLag = Meter.CreateHistogram<double>("consumer_lag");
}
