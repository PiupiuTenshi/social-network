using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace Account.Infrastructure.Persistence;

public sealed class AccountDbContextFactory : IDesignTimeDbContextFactory<AccountDbContext>
{
    public AccountDbContext CreateDbContext(string[] args)
    {
        var options = new DbContextOptionsBuilder<AccountDbContext>()
            .UseSqlite("Data Source=work/toolchain-migration/design-time.db")
            .Options;

        return new AccountDbContext(options);
    }
}
