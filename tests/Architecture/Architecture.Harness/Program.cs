using System.Xml.Linq;
using Account.Domain;

var root = FindRepositoryRoot();
var domainProject = Path.Combine(root, "src", "Services", "Account", "Account.Domain", "Account.Domain.csproj");
var document = XDocument.Load(domainProject);

if (document.Descendants("PackageReference").Any())
{
    throw new InvalidOperationException("Domain must not reference packages.");
}

var forbiddenTokens = new[] { "EntityFramework", "AspNetCore", "Kafka", "SignalR", "Http" };
var projectText = File.ReadAllText(domainProject);
if (forbiddenTokens.Any(projectText.Contains))
{
    throw new InvalidOperationException("Domain project contains a framework dependency token.");
}

var references = typeof(DomainMarker).Assembly.GetReferencedAssemblies().Select(reference => reference.Name ?? string.Empty);
if (references.Any(name => forbiddenTokens.Any(token => name.Contains(token, StringComparison.OrdinalIgnoreCase))))
{
    throw new InvalidOperationException("Compiled Domain assembly references a forbidden framework assembly.");
}

Console.WriteLine("Architecture harness passed: Account.Domain is framework-free.");

static string FindRepositoryRoot()
{
    var current = new DirectoryInfo(Directory.GetCurrentDirectory());
    while (current is not null)
    {
        if (File.Exists(Path.Combine(current.FullName, "global.json")))
        {
            return current.FullName;
        }

        current = current.Parent;
    }

    throw new DirectoryNotFoundException("Repository root containing global.json was not found.");
}
