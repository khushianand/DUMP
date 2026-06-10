# GUI Assets

Place GUI images, icons, and GIF illustrations here so `vulnerability_gui_pyqt.py` can load them with repository-relative paths.

## Expected structure

```text
assets/
  icons/
    shield.svg                  # Header/window security icon
  kpi/
    file-shield.svg             # Vulnerabilities processed card
    shield.svg                  # Unique vulnerabilities card
    clock.svg                   # Processing time card
    trending-up.svg             # Success rate card
  illustrations/
    sidebar-light.svg           # Light theme sidebar illustration
    sidebar-dark.svg            # Dark theme sidebar illustration
    security-dashboard.svg      # Legacy/fallback illustration
  decorations/
    dot-grid.svg                # Light background decoration candidate
    wave-mesh.svg               # Dark background decoration candidate
  gifs/
    security-loop.gif           # Optional animated sidebar GIF
```

The app attempts to load `assets/gifs/security-loop.gif` first for the sidebar illustration. If the GIF is not present, it uses `assets/illustrations/sidebar-light.svg` or `assets/illustrations/sidebar-dark.svg` depending on the active theme, then falls back to text if no image can be loaded. KPI cards load SVG icons from `assets/kpi`.
