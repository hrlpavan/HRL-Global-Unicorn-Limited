# HRL International Private Limited™ — Master Brand Design System & UI/UX Engineering Guidelines
**Document Status**: Official Corporate Standard (Single Source of Truth for All Projects)  
**Entity**: HRL International Private Limited™  
**Founder & Managing Director**: Pavan Kumar Sadashiv (B.E. CSE AIML, SCEM Mangaluru)  
**Company Motto**: *"We Can Do Everything Related To Software Sector Without Any Excuses!"*  
**Effective Date**: August 2026  
**Scope**: Applicable to all Web Applications, SaaS Dashboards, 4K Showcase Suites, AI Tools, Mobile UIs, and GitHub Codebases.  

---

## 1. Core Brand Identity & Non-Negotiable Operating Principles

Every software, web, and media project created under **HRL International** must strictly comply with these foundational rules:

1. **Strict 100% Zero-Emoji Policy**:
   * Decorative emojis (such as , , , ) are strictly prohibited in all production HTML, CSS, JavaScript, and corporate documentation.
   * Visual icons must solely be rendered as clean SVG vector icons (Lucide/Heroicons standard) or high-resolution brand assets.
2. **Apple-Caliber Executive Minimalist Aesthetic**:
   * High contrast, generous whitespace, subtle 1px translucent borders, and soft shadows.
   * Fluid transitions (0.2s to 0.3s ease) on all interactive hover and focus states.
3. **The Symmetrical Placing Principle**:
   * Grids must maintain geometric balance:
     * **4 Items**: Balanced **2×2 grid on desktop**, 1-column on mobile.
     * **3 Items**: Balanced **3-column Bento grid on desktop**, 1-column on mobile.
     * **2 Items**: Balanced **50/50 or 60/40 split**.
   * Never leave a lone, dangling card on a second row.
4. **Mandatory Company Motto Placement**:
   * Every flagship application must prominently feature the official company motto badge:  
     `"We Can Do Everything Related To Software Sector Without Any Excuses!"`
5. **Mandatory Frontend Code Protection**:
   * Every public frontend must include the client-side `security-shield.js` to block unauthorized context menus, F12 inspection, and DevTools shortcuts.

---

## 2. Master Color Palette & Design Tokens

### A. Primary Brand Palette
| Token Name | Hex Code | RGB / HSL | Usage Description |
| :--- | :--- | :--- | :--- |
| `--hrl-crimson` | `#D1002D` | `rgb(209, 0, 45)` | Primary brand color, primary CTA buttons, active accents, brand logo. |
| `--hrl-crimson-dark` | `#A50024` | `rgb(165, 0, 36)` | Button hover state, active click state. |
| `--hrl-crimson-tint` | `rgba(209, 0, 45, 0.08)` | — | Badge backgrounds, highlighted table cells, active card borders. |
| `--hrl-crimson-glow` | `rgba(209, 0, 45, 0.25)` | — | Hover drop-shadows, focus outlines, glow borders. |

### B. Dark Theme (Cinema & OLED Pro Standard)
| Token Name | Hex Code | Usage Description |
| :--- | :--- | :--- |
| `--bg-dark-oled` | `#000000` | Deepest pitch black (Video player background, hero cinema background). |
| `--bg-dark-base` | `#0A0A0C` | Primary dark mode surface background. |
| `--bg-dark-surface` | `#121216` | Card background, modal background, sidebar background. |
| `--bg-dark-elevated`| `#1C1C22` | Card hover state, dropdown menus, floating action docks. |
| `--border-dark-subtle`| `rgba(255, 255, 255, 0.08)` | 1px clean card border, divider lines. |
| `--border-dark-hover` | `rgba(255, 255, 255, 0.18)` | Interactive border state upon hover. |
| `--text-dark-primary` | `#FFFFFF` | Primary headers and high-contrast titles. |
| `--text-dark-secondary`| `#A1A1AA` | Body paragraphs, secondary specs, subtitle text. |
| `--text-dark-muted`   | `#71717A` | Metadata, tags, dates, footer copyright text. |

### C. Light Theme (Corporate & Executive Standard)
| Token Name | Hex Code | Usage Description |
| :--- | :--- | :--- |
| `--bg-light-base` | `#FFFFFF` | Clean pure white page background. |
| `--bg-light-surface`| `#F5F5F7` | Apple light slate card background, spec pane background. |
| `--border-light`    | `rgba(0, 0, 0, 0.06)` | Ultra-clean subtle card border. |
| `--border-light-hover`| `rgba(0, 0, 0, 0.14)` | Hover card border. |
| `--text-light-dark` | `#1D1D1F` | Deep charcoal primary text (never use harsh #000 on white). |
| `--text-light-body` | `#515154` | Secondary body text. |
| `--text-light-muted`| `#86868B` | Eyebrows, uppercase metadata, timestamp indicators. |

---

## 3. Typography Scale & Hierarchy (SF Pro System)

### A. Font Families
* **Primary Display & Text**:  
  `font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;`
* **Code & Monospace**:  
  `font-family: ui-monospace, "SF Mono", "Cascadia Code", "Roboto Mono", Menlo, Consolas, monospace;`

### B. Type Scale Ratios & Specs
| Element | Font Size | Line Height | Letter Spacing | Font Weight | Text Transform |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero Title (H1)** | `clamp(32px, 5.5vw, 56px)` | `1.08` | `-0.03em` | `800` (Bold/Heavy) | None |
| **Section Title (H2)**| `clamp(24px, 4vw, 36px)` | `1.2` | `-0.02em` | `700` (Bold) | None |
| **Card Title (H3)** | `18px - 20px` | `1.3` | `-0.015em` | `700` (Bold) | None |
| **Subhead / Lead** | `17px - 19px` | `1.45` | `-0.01em` | `400 / 500` | None |
| **Body Paragraph** | `13.5px - 15px` | `1.55` | `0em` | `400 / 500` | None |
| **Eyebrow Tag** | `11px - 12px` | `1.2` | `+0.06em to 0.08em`| `600 / 700` | `uppercase` |
| **Micro Copy / Legal**| `11px - 12px` | `1.4` | `0em` | `400` | None |

---

## 4. Geometric Ratios, Spacing & Layout Architecture

### A. Aspect Ratios for Media & Components
* **Cinema Video Players & Showcases**: `16:9` (`aspect-ratio: 16 / 9;`)
* **Hero Showcases / Ultrawide Banners**: `21:9` (`aspect-ratio: 21 / 9;`)
* **Company Logos & Brand Avatars**: `1:1` Square (`width: 32px; height: 32px;` or `48px × 48px; object-fit: contain;`)
* **Data & Metric Infographics**: `1:1` or `4:5`

### B. Border Radii Standards
* **Pill Badges & CTA Buttons**: `9999px` (Full Pill)
* **Standard Interactive Cards**: `16px - 18px`
* **Large Containers / Video Theaters**: `24px`
* **Dropdown Menus & Tooltips**: `10px - 12px`

### C. Container Max-Widths
* **Global Navigation**: `max-width: 1200px;` (or `100%` with `padding: 0 24px;`)
* **Standard Content Sections**: `max-width: 1024px; margin: 0 auto;`
* **Wide Cinema & Showcase Views**: `max-width: 1280px; margin: 0 auto;`

---

## 5. UI Component Specifications (Ready-to-Use Patterns)

### Pattern 1: Official Company Motto Hero Pill
```html
<div class="company-motto-badge">
  <span class="motto-tag">Company Motto</span>
  <span class="motto-text">We Can Do Everything Related To Software Sector Without Any Excuses!</span>
</div>
```
```css
/* Apple-Caliber Executive Company Motto Badge */
.company-motto-badge {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.08);
  padding: 5px 18px 5px 6px;
  border-radius: 9999px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  margin-bottom: 24px;
  vertical-align: middle;
}
.company-motto-badge:hover {
  border-color: rgba(0, 0, 0, 0.14);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
  transform: translateY(-1px);
}
.motto-tag {
  background: linear-gradient(135deg, #D1002D 0%, #B80026 100%);
  color: #FFFFFF;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 4px 11px;
  border-radius: 9999px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  box-shadow: 0 1px 3px rgba(209, 0, 45, 0.28);
  flex-shrink: 0;
}
.motto-text {
  color: #1D1D1F;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: -0.012em;
  line-height: 1;
  display: inline-flex;
  align-items: center;
}
@media (max-width: 640px) {
  .company-motto-badge {
    padding: 6px 14px 6px 6px;
    gap: 8px;
    max-width: 100%;
    text-align: left;
  }
}
```

---

### Pattern 2: Balanced 2×2 Symmetrical Knowledge Card Grid
```html
<div class="entity-cards-grid">
  <div class="entity-info-card">
    <div class="entity-card-eyebrow">Category Tag</div>
    <div class="entity-card-title">Card Header Title</div>
    <p class="entity-card-desc">Concise, high-impact description formatted with uniform line height and typography.</p>
  </div>
  <!-- Exactly 4 cards structured symmetrically -->
</div>
```
```css
.entity-cards-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}
@media (min-width: 768px) {
  .entity-cards-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
  }
}
.entity-info-card {
  background: #f5f5f7;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 18px;
  padding: 24px 26px;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.entity-info-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.04);
  border-color: rgba(0, 0, 0, 0.12);
}
.entity-card-eyebrow {
  font-size: 11px;
  color: #86868b;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 8px;
}
.entity-card-title {
  font-size: 18px;
  font-weight: 700;
  color: #1d1d1f;
  letter-spacing: -0.015em;
  line-height: 1.3;
  margin-bottom: 8px;
}
.entity-card-desc {
  font-size: 13.5px;
  color: #515154;
  line-height: 1.55;
  margin: 0;
}
```

---

### Pattern 2.1: Full-Width Rectangular Sovereign Flag Showcase Card
Use whenever displaying the Sovereign Corporate Flag within an entity grid, spanning full width (`grid-column: 1 / -1;`) with two-column content + RAW visual layout to eliminate wasted space.
```html
<div class="entity-flag-rectangle-card">
  <div class="entity-flag-info">
    <div class="entity-card-eyebrow" style="color: #BF1F1F; font-weight: 700;">Sovereign Corporate Flag &amp; Vexillological Standard</div>
    <div class="entity-card-title" style="font-size: 22px; font-weight: 800; margin-bottom: 8px;">
      <a href="flag.html" style="color: inherit; text-decoration: none;">Official HRL Sovereign Corporate Flag</a>
    </div>
    <p class="entity-card-desc" style="font-size: 14px; line-height: 1.6; color: #515154;">
      Official sovereign flag specifications, heraldic geometry, and vector standard.
    </p>
    <div class="entity-flag-badges">
      <span class="entity-flag-badge primary">Nordic Cross 83px Grid</span>
      <span class="entity-flag-badge">RAW Ultra-HD (10,800 × 7,200 px)</span>
    </div>
    <div class="entity-flag-actions">
      <a href="flag.html" class="apple-btn-primary">Explore Flag Portal &rarr;</a>
      <a href="assets/HRL%20INTERNATIONAL%20PRIVATE%20LIMITED%20CORE%20COUNTRY%20FLAG.png" download class="apple-btn-secondary">Download RAW Master &darr;</a>
    </div>
  </div>
  <div class="entity-flag-preview-column">
    <a href="flag.html" class="entity-flag-preview-wrapper" title="Explore Official Corporate Flag">
      <img src="assets/HRL%20INTERNATIONAL%20PRIVATE%20LIMITED%20CORE%20COUNTRY%20FLAG.png" alt="HRL Official Flag" class="entity-flag-preview-img" />
    </a>
  </div>
</div>
```
```css
.entity-flag-rectangle-card {
  grid-column: 1 / -1;
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-top: 3px solid #BF1F1F;
  border-radius: 18px;
  padding: 30px;
  display: grid;
  grid-template-columns: 1fr;
  gap: 28px;
  align-items: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
}
@media (min-width: 860px) {
  .entity-flag-rectangle-card {
    grid-template-columns: 1.3fr 1fr;
    gap: 36px;
  }
}
.entity-flag-rectangle-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.06);
  border-color: rgba(0, 0, 0, 0.14);
}
.entity-flag-preview-wrapper {
  display: block;
  width: 100%;
  aspect-ratio: 3 / 2;
  border-radius: 12px;
  overflow: hidden;
  background: #BF1F1F;
  border: 1px solid rgba(0, 0, 0, 0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  text-decoration: none;
}
.entity-flag-preview-wrapper:hover {
  transform: scale(1.015);
  box-shadow: 0 8px 24px rgba(191, 31, 31, 0.18);
}
.entity-flag-preview-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  box-shadow: none !important;
  border: none !important;
}
```

---

### Pattern 3: Primary Crimson CTA Button
```html
<a href="#action" class="hrl-btn-primary">
  <span>Explore Showcase</span>
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
</a>
```
```css
.hrl-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: #D1002D;
  color: #ffffff;
  font-size: 13.5px;
  font-weight: 600;
  padding: 10px 22px;
  border-radius: 9999px;
  text-decoration: none;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(209, 0, 45, 0.25);
  transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
}
.hrl-btn-primary:hover {
  background: #A50024;
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(209, 0, 45, 0.35);
}
```

---

## 6. Statutory Legal Footer Standard

Every project must terminate with the official statutory intellectual property statement:

```html
<footer class="hrl-footer">
  <div class="footer-legal-container">
    <p>Copyright &copy; 2026 Pavan Kumar Sadashiv. HRL International&trade; and HRL International Private Limited&trade; are asserted trademarks of Pavan Kumar Sadashiv. Mangaluru, Karnataka, India. All rights reserved.</p>
    <div class="footer-nav-links">
      <a href="index.html">Corporate Entity</a>
      <span>&bull;</span>
      <a href="showcase.html">4K Showcase</a>
      <span>&bull;</span>
      <a href="https://github.com/hrlpavan" target="_blank" rel="noopener noreferrer">GitHub</a>
      <span>&bull;</span>
      <a href="COPYRIGHT_AND_DMCA_POLICY.md" target="_blank" rel="noopener noreferrer">Copyright &amp; DMCA Policy</a>
    </div>
  </div>
</footer>
```

---

## 7. Ready-to-Drop CSS Variables (`design-tokens.css`)

Copy this master block directly into the `:root` of any new frontend project:

```css
:root {
  /* Brand Accents */
  --hrl-red: #D1002D;
  --hrl-red-dark: #A50024;
  --hrl-red-tint: rgba(209, 0, 45, 0.08);
  --hrl-red-border: rgba(209, 0, 45, 0.28);
  --hrl-red-glow: rgba(209, 0, 45, 0.25);

  /* Light Theme Surfaces & Text */
  --surface-light-bg: #FFFFFF;
  --surface-light-card: #F5F5F7;
  --surface-light-border: rgba(0, 0, 0, 0.06);
  --text-primary-dark: #1D1D1F;
  --text-secondary-dark: #515154;
  --text-muted-dark: #86868B;

  /* Dark Theme Surfaces & Text */
  --surface-dark-oled: #000000;
  --surface-dark-base: #0A0A0C;
  --surface-dark-card: #121216;
  --surface-dark-elevated: #1C1C22;
  --surface-dark-border: rgba(255, 255, 255, 0.08);
  --text-primary-light: #FFFFFF;
  --text-secondary-light: #A1A1AA;
  --text-muted-light: #71717A;

  /* Typography */
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "Cascadia Code", "Roboto Mono", monospace;

  /* Radius Standards */
  --radius-pill: 9999px;
  --radius-card: 18px;
  --radius-modal: 24px;
  --radius-sm: 10px;

  /* Transitions */
  --transition-fast: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
```

---
*Maintained and enforced across all codebases under HRL International Private Limited.*
