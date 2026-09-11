import { readFileSync } from 'node:fs';

const read = (path) => readFileSync(new URL(path, import.meta.url), 'utf8');
const shell = read('../src/app/shell/shell.component.html');
const styles = read('../src/app/shell/shell.component.scss');
const routes = read('../src/app/app.routes.ts');
const flags = read('../src/app/core/feature-flags.ts');
const globalStyles = read('../src/styles.scss');
const tokens = JSON.parse(read('../../design/tokens/design-tokens.json'));

const luminance = (hex) => {
  const channels = hex
    .slice(1)
    .match(/.{2}/g)
    .map((part) => Number.parseInt(part, 16) / 255);
  const [red, green, blue] = channels.map((value) =>
    value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4,
  );
  return 0.2126 * red + 0.7152 * green + 0.0722 * blue;
};
const contrast = (foreground, background) => {
  const [lighter, darker] = [luminance(foreground), luminance(background)].sort((a, b) => b - a);
  return (lighter + 0.05) / (darker + 0.05);
};
const contrastPasses = [
  [
    'light text contrast',
    contrast(tokens.color.light.text.$value, tokens.color.light.background.$value) >= 4.5,
  ],
  [
    'dark text contrast',
    contrast(tokens.color.dark.text.$value, tokens.color.dark.background.$value) >= 4.5,
  ],
];
const required = [
  ['skip link', shell.includes('skip-link') && shell.includes('#main-content')],
  ['accessible navigation', shell.includes('aria-label="Điều hướng chính"')],
  [
    'button targets',
    styles.includes('min-block-size: var(--sp-size-touch-target)') &&
      styles.includes('min-inline-size: var(--sp-size-touch-target)'),
  ],
  ['visible focus', styles.includes(':focus-visible')],
  ['reduced motion', styles.includes('prefers-reduced-motion: reduce')],
  ['desktop/mobile shell layout', styles.includes('grid-template-columns') && styles.includes('@media (max-width: 48rem)')],
  ['safe fallback route', routes.includes("path: '**', redirectTo: '/home'")],
  ['disabled P2 feature', flags.includes('marketplace: false')],
  ['disabled feature guarded', routes.includes("featureEnabledGuard('marketplace')")],
  ['generated design tokens imported', globalStyles.includes('tokens.generated.css')],
];
const failures = [...required, ...contrastPasses]
  .filter(([, passed]) => !passed)
  .map(([name]) => name);
if (failures.length) throw new Error(`Foundation checks failed: ${failures.join(', ')}`);
console.log(
  `Foundation accessibility/route checks passed: ${required.length + contrastPasses.length}`,
);
