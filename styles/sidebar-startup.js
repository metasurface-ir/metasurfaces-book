/* Apply saved panel preferences before the first paint without changing the
   HTML that MyST's React root will hydrate. The normal controls take over
   as soon as they set their corresponding data attributes. */
(() => {
  try {
    const saved = JSON.parse(localStorage.getItem('metasurface-book-sidebars') || '{}');
    const rules = [];
    if (saved?.navigation) {
      rules.push(`
        @media (min-width: 1280px) {
          html:not([data-book-navigation]) {
            --book-nav-width: 0px !important;
            --book-nav-gap: 0px !important;
            --book-nav-space: 0rem !important;
          }
          html:not([data-book-navigation]) .myst-primary-sidebar { display: none !important; }
        }
      `);
    }
    if (saved?.outline) {
      rules.push(`
        html:not([data-book-outline]) {
          --book-outline-width: 0px !important;
          --book-outline-gap: 0px !important;
          --book-outline-space: 0rem !important;
        }
        html:not([data-book-outline]) article > div:has(> .myst-outline-section) { display: none !important; }
      `);
    }
    if (rules.length) {
      const sheet = new CSSStyleSheet();
      sheet.replaceSync(rules.join('\n'));
      document.adoptedStyleSheets = [...document.adoptedStyleSheets, sheet];
    }
  } catch {
    // The book still opens with its default panels if storage is unavailable.
  }
})();
