import { inject } from '@angular/core';
import { CanMatchFn, Router } from '@angular/router';
import { FeatureName, featureFlags } from './feature-flags';

export const featureEnabledGuard =
  (feature: FeatureName): CanMatchFn =>
  () => {
    const router = inject(Router);
    return featureFlags[feature] ? true : router.parseUrl('/home');
  };
