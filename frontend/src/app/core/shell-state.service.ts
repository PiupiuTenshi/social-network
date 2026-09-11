import { Injectable, computed, signal } from '@angular/core';

export type Theme = 'light' | 'dark';

@Injectable({ providedIn: 'root' })
export class ShellStateService {
  readonly theme = signal<Theme>('light');
  readonly navigationOpen = signal(false);
  readonly online = signal(true);
  readonly themeLabel = computed(() =>
    this.theme() === 'light' ? 'Bật giao diện tối' : 'Bật giao diện sáng',
  );
  toggleNavigation(): void {
    this.navigationOpen.update((open) => !open);
  }
  closeNavigation(): void {
    this.navigationOpen.set(false);
  }
  toggleTheme(): void {
    this.theme.update((theme) => (theme === 'light' ? 'dark' : 'light'));
  }
}
