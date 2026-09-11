using Microsoft.EntityFrameworkCore;

namespace Account.Infrastructure.Persistence;

/// <summary>Empty EF Core boundary used only to prove migration tooling.</summary>
public sealed class AccountDbContext(DbContextOptions<AccountDbContext> options) : DbContext(options)
{
    public DbSet<OutboxRecord> Outbox => Set<OutboxRecord>();
    public DbSet<InboxRecord> Inbox => Set<InboxRecord>();
    public DbSet<IdempotencyRecord> Idempotency => Set<IdempotencyRecord>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<OutboxRecord>(entity =>
        {
            entity.ToTable("outbox_message");
            entity.HasKey(record => record.EventId);
            entity.Property(record => record.EventType).HasMaxLength(200);
            entity.Property(record => record.CorrelationId).HasMaxLength(128);
            entity.Property(record => record.Payload).HasColumnType("TEXT");
            entity.HasIndex(record => new { record.PublishedAt, record.OccurredAt });
        });
        modelBuilder.Entity<InboxRecord>(entity => { entity.ToTable("inbox_message"); entity.HasKey(record => record.EventId); });
        modelBuilder.Entity<IdempotencyRecord>(entity => { entity.ToTable("idempotency_record"); entity.HasKey(record => record.Key); entity.Property(record => record.Key).HasMaxLength(128); entity.HasIndex(record => record.ExpiresAt); });
    }
}
