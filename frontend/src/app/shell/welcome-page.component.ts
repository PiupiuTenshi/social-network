import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-welcome-page',
  template: `<section class="welcome" aria-labelledby="page-title">
    <p class="eyebrow">Nền tảng giao diện</p>
    <h1 id="page-title">Twight Light</h1>
    <p>
      App shell đã sẵn sàng. Các màn hình nghiệp vụ chỉ xuất hiện khi hợp đồng tương ứng được nghiệm
      thu.
    </p>
    <a class="primary-action" href="#main-content">Tiếp tục</a>
  </section>`,
  styles: [
    `
      .welcome {
        background: var(--color-surface);
        border: 1px solid var(--color-border);
        border-radius: var(--radius-md);
        max-inline-size: 44rem;
        padding: clamp(1.5rem, 5vw, 4rem);
      }
      .eyebrow {
        color: var(--color-brand);
        font-weight: 700;
        margin: 0 0 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-size: 0.75rem;
      }
      h1 {
        font-size: clamp(2rem, 7vw, 4rem);
        line-height: 1;
        margin: 0;
      }
      p {
        color: var(--color-text-muted);
        line-height: 1.6;
        max-inline-size: 55ch;
      }
      .primary-action {
        align-items: center;
        background: var(--color-brand);
        border-radius: var(--radius-sm);
        color: #fff;
        display: inline-flex;
        font-weight: 700;
        margin-block-start: 1.5rem;
        min-block-size: var(--sp-size-touch-target);
        padding-inline: 1rem;
        text-decoration: none;
      }
    `,
  ],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class WelcomePageComponent {}
