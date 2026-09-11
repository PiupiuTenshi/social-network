using Account.Infrastructure.Persistence;
using Account.Infrastructure.Messaging;
using Microsoft.Data.Sqlite;
using Microsoft.EntityFrameworkCore;

var databaseDirectory = Path.Combine(Directory.GetCurrentDirectory(), "work", "toolchain-migration");
Directory.CreateDirectory(databaseDirectory);
var databasePath = Path.Combine(databaseDirectory, $"empty-migration-{Guid.NewGuid():N}.db");

var connectionString = new SqliteConnectionStringBuilder { DataSource = databasePath }.ToString();
var options = new DbContextOptionsBuilder<AccountDbContext>()
    .UseSqlite(connectionString)
    .Options;

await using var context = new AccountDbContext(options);
await context.Database.MigrateAsync();

var appliedMigrations = await context.Database.GetAppliedMigrationsAsync();
if (!appliedMigrations.Any(migration => migration.EndsWith("InitialEmpty", StringComparison.Ordinal)))
{
    throw new InvalidOperationException("The empty InitialEmpty migration was not applied.");
}

var eventId = Guid.CreateVersion7();
var effects = 0;
var processor = new AccountInboxProcessor(context);
var first = await processor.ProcessOnceAsync(eventId, _ => { effects++; return Task.CompletedTask; }, CancellationToken.None);
var duplicate = await processor.ProcessOnceAsync(eventId, _ => { effects++; return Task.CompletedTask; }, CancellationToken.None);
if (!first || duplicate || effects != 1 || await context.Inbox.CountAsync() != 1)
{
    throw new InvalidOperationException("Inbox idempotency transaction failed.");
}

try
{
    await using var transaction = await context.Database.BeginTransactionAsync();
    context.Outbox.Add(new OutboxRecord { EventId = Guid.CreateVersion7(), EventType = "FaultProbe", EventVersion = 1, OccurredAt = DateTimeOffset.UtcNow, CorrelationId = "fault-probe", AggregateId = Guid.CreateVersion7(), AggregateVersion = 1, Payload = "{}" });
    await context.SaveChangesAsync();
    throw new InvalidOperationException("Simulated database failure before commit.");
}
catch (InvalidOperationException)
{
    context.ChangeTracker.Clear();
}
if (await context.Outbox.AnyAsync()) throw new InvalidOperationException("Rolled-back database work produced an Outbox event.");

Console.WriteLine($"Migration/platform harness passed: {Path.GetFileName(databasePath)}");
