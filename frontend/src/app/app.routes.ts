import { Routes } from '@angular/router';

import { featureEnabledGuard } from './core/feature-enabled.guard';
import { ShellComponent } from './shell/shell.component';
import { WelcomePageComponent } from './shell/welcome-page.component';

export const routes: Routes = [
  {
    path: '',
    component: ShellComponent,
    children: [
      { path: '', pathMatch: 'full', redirectTo: 'home' },
      { path: 'home', component: WelcomePageComponent, title: 'Trang chủ | Twight Light' },
      { path: 'discover', component: WelcomePageComponent, title: 'Khám phá | Twight Light' },
      { path: 'notifications', component: WelcomePageComponent, title: 'Thông báo | Twight Light' },
      { path: 'messages', component: WelcomePageComponent, title: 'Tin nhắn | Twight Light' },
      { path: 'profile', component: WelcomePageComponent, title: 'Hồ sơ | Twight Light' },
      { path: 'settings', component: WelcomePageComponent, title: 'Cài đặt | Twight Light' },
      {
        path: 'marketplace',
        canMatch: [featureEnabledGuard('marketplace')],
        component: WelcomePageComponent,
      },
    ],
  },
  { path: '**', redirectTo: '/home' },
];
