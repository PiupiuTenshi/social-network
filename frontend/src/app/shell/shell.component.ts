import { ChangeDetectionStrategy, Component, HostBinding, inject } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { ShellStateService } from '../core/shell-state.service';

interface NavigationItem {
  label: string;
  route: string;
  icon: string;
}

@Component({
  selector: 'app-shell',
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  templateUrl: './shell.component.html',
  styleUrl: './shell.component.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ShellComponent {
  readonly state = inject(ShellStateService);
  readonly navigation: readonly NavigationItem[] = [
    { label: 'Trang chủ', route: '/home', icon: '⌂' },
    { label: 'Khám phá', route: '/discover', icon: '⌕' },
    { label: 'Thông báo', route: '/notifications', icon: '◌' },
    { label: 'Tin nhắn', route: '/messages', icon: '✉' },
    { label: 'Hồ sơ', route: '/profile', icon: '◉' },
    { label: 'Cài đặt', route: '/settings', icon: '⚙' },
  ];
  @HostBinding('attr.data-theme') get theme(): string {
    return this.state.theme();
  }
}
