using Account.Infrastructure.Persistence;
using Microsoft.EntityFrameworkCore;

namespace Account.Infrastructure.Messaging;

public sealed class AccountInboxProcessor(AccountDbContext db)
{
    public async Task<bool> ProcessOnceAsync(Guid eventId, Func<CancellationToken, Task> sideEffect, CancellationToken cancellationToken)
    {
        await using var transaction = await db.Database.BeginTransactionAsync(cancellationToken);
        if (await db.Inbox.AnyAsync(record => record.EventId == eventId, cancellationToken))
        {
            await transaction.RollbackAsync(cancellationToken);
            return false;
        }
        db.Inbox.Add(new InboxRecord { EventId = eventId, ProcessedAt = DateTimeOffset.UtcNow });
        await sideEffect(cancellationToken);
        await db.SaveChangesAsync(cancellationToken);
        await transaction.CommitAsync(cancellationToken);
        return true;
    }
}
