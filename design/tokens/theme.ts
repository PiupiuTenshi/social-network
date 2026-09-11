export const socialPlatformTheme = {
  colors: {
    brand: { 50: "#eef2ff", 100: "#e0e7ff", 500: "#6366f1", 600: "#4f46e5", 700: "#4338ca" },
    accent: { 500: "#06b6d4", 600: "#0891b2" },
    neutral: {
      0: "#ffffff", 50: "#f8fafc", 100: "#f1f5f9", 200: "#e2e8f0",
      300: "#cbd5e1", 500: "#64748b", 600: "#475569", 700: "#334155",
      800: "#1e293b", 900: "#0f172a", 950: "#020617"
    },
    success: "#15803d",
    warning: "#b45309",
    danger: "#b91c1c"
  },
  spacing: { 1: "4px", 2: "8px", 3: "12px", 4: "16px", 5: "20px", 6: "24px", 8: "32px", 10: "40px", 12: "48px", 16: "64px" },
  borderRadius: { sm: "8px", md: "12px", lg: "16px", xl: "20px", full: "999px" },
  screens: { mobile: "640px", tablet: "1024px", wide: "1200px" }
} as const;
