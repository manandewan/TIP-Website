---
name: mobile-browser-audit
description: Rigorous audit and testing suite to verify whether a website works seamlessly on mobile browsers. Audits viewport responsiveness, horizontal overflow across 320px-430px widths, touch target sizing (44x44px), iOS Safari auto-zoom prevention, tap delay optimization, safe-area notches, and WCAG contrast.
metadata:
  author: tip-engineering
  version: "1.0.0"
---

# Mobile Browser Audit & Verification Skill

This skill provides automated tests and inspection procedures to guarantee seamless mobile browser performance, ergonomics, and visual integrity before deploying to production.

## Core Mobile Verification Rules

### 1. Viewport & Safe Areas
- Viewport tag must include `viewport-fit=cover`:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  ```
- Support device notches and home indicator bars:
  ```css
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
  padding-left: env(safe-area-inset-left, 0px);
  padding-right: env(safe-area-inset-right, 0px);
  ```
- Theme color meta tag matching header/background:
  ```html
  <meta name="theme-color" content="#030712">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  ```

### 2. Zero Horizontal Overflow
- Across all standard mobile widths:
  - **320px** (iPhone SE 1st gen / ultra-narrow)
  - **375px** (iPhone mini / SE 2nd/3rd gen)
  - **390px** (iPhone 12 / 13 / 14 / 15 standard)
  - **414px** (iPhone Plus / XR / Max standard)
  - **430px** (iPhone 14 / 15 / 16 Pro Max)
- `document.documentElement.scrollWidth <= window.innerWidth` at all times.
- Root protection: `overflow-x: hidden; width: 100%;` on `html, body`.
- Preventions:
  - Long strings and URLs must have `overflow-wrap: anywhere; word-break: break-word;`.
  - Media/images must have `max-width: 100%; height: auto; display: block;`.
  - Flex child text containers must have `min-width: 0;` to avoid blowing out flex parent width.

### 3. Touch Targets & Ergonomics
- All tap targets (`<a>`, `<button>`, inputs, clickable cards) must be at least **44 × 44px** per Apple Human Interface Guidelines (or min 48 × 48px per Google Material).
- Use `touch-action: manipulation;` to eliminate the 300ms double-tap-to-zoom delay on iOS and Android.
- Spacing between adjacent touch targets must be >= 8px to prevent mis-taps.
- Custom tap highlight feedback:
  ```css
  -webkit-tap-highlight-color: rgba(217, 119, 6, 0.2);
  ```

### 4. iOS Safari Auto-Zoom Prevention
- Text inputs, textareas, and selects must have `font-size: 16px` or larger. Any `font-size < 16px` triggers iOS Safari to aggressively zoom in on focus, breaking page framing and user orientation.

### 5. Smooth Scrolling & Gestures
- Momentum scrolling on iOS: `-webkit-overflow-scrolling: touch;`.
- Prevent pull-to-refresh interference on fixed/dialog overlays: `overscroll-behavior: contain;`.

### 6. Contrast & Readability
- Body text contrast >= 4.5:1 (WCAG AA).
- Large headings >= 3:1.
- Distinct card boundaries with frosted glass borders (`rgba(255, 255, 255, 0.12)` or vibrant accent borders).

---

## Automated Audit Script

Run the automated test suite against your local server or production URL:

```bash
python3 .agents/skills/mobile-browser-audit/scripts/audit_mobile.py --url http://localhost:8099
```

The script connects to headless Google Chrome, simulates all target screen sizes via Chrome DevTools Protocol, inspects DOM elements for overflow and sizing violations, and generates a structured pass/fail report.
