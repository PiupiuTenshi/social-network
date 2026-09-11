using System.Threading.RateLimiting;
using Microsoft.AspNetCore.RateLimiting;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddProblemDetails();
builder.Services.AddRateLimiter(options => options.AddFixedWindowLimiter("api", limiter =>
{
    limiter.PermitLimit = 100;
    limiter.Window = TimeSpan.FromMinutes(1);
    limiter.QueueLimit = 0;
}));
var app = builder.Build();

app.UseExceptionHandler();
app.UseRateLimiter();

app.Use(async (context, next) =>
{
    var correlationId = context.Request.Headers["X-Correlation-ID"].FirstOrDefault();
    if (string.IsNullOrWhiteSpace(correlationId) || correlationId.Length > 128)
    {
        correlationId = Guid.CreateVersion7().ToString();
    }

    context.TraceIdentifier = correlationId;
    context.Response.Headers["X-Correlation-ID"] = correlationId;
    await next(context);
});

app.MapGet("/healthz", (HttpContext context) => Results.Ok(new { status = "ok", traceId = context.TraceIdentifier })).RequireRateLimiting("api");

app.Run();
