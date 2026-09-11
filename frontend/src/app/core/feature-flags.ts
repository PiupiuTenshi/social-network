export type FeatureName = 'marketplace' | 'aiSearch' | 'media';

/** Features without accepted contracts stay disabled and absent from navigation. */
export const featureFlags: Readonly<Record<FeatureName, boolean>> = {
  marketplace: false,
  aiSearch: false,
  media: false,
};
