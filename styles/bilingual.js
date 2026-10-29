/* Language changes use a full navigation: each edition has its own MyST router. */
(() => {
  'use strict';
  const config = JSON.parse(document.getElementById('book-language-config').textContent);
  const fa = config.language === 'fa', language = fa ? 'fa' : 'en';
  const words = {
    'Table of Contents': 'فهرست مطالب', 'Navigation': 'ناوبری', 'On this page': 'در این صفحه',
    'Search': 'جست‌وجو', 'Search…': 'جست‌وجو…', 'Search...': 'جست‌وجو…',
    'Search the book': 'جست‌وجو در کتاب', 'Search documentation': 'جست‌وجو در کتاب',
    'Previous': 'قبلی', 'Next': 'بعدی', 'Contents': 'فهرست',
    'Copy to clipboard': 'کپی', 'Copy code': 'کپی کد', 'Copied!': 'کپی شد!',
    'Download': 'دریافت', 'Downloads': 'دریافت فایل‌ها', 'Edit this page': 'ویرایش این صفحه',
    'Open menu': 'باز کردن فهرست', 'Close menu': 'بستن فهرست',
    'Toggle theme': 'تغییر ظاهر', 'Toggle navigation': 'نمایش فهرست',
    'Light': 'روشن', 'Dark': 'تیره', 'System': 'سیستم',
    'Made with MyST': 'ساخته‌شده با MyST', 'Back to top': 'بازگشت به بالا'
  };
  Object.assign(words, {
    'Open Menu': 'باز کردن فهرست', 'Close Menu': 'بستن فهرست',
    'Open Contents': 'باز کردن فهرست این صفحه', 'Close Contents': 'بستن فهرست این صفحه',
    'Open Folder': 'باز کردن بخش', 'Close Folder': 'بستن بخش',
    'Toggle theme between light and dark mode': 'تغییر ظاهر روشن و تیره',
    'CONTENTS': 'فهرست این صفحه', 'Search Website': 'جست‌وجو در کتاب',
    'Search articles and their contents using fuzzy-search and prefix-matching': 'عنوان و متن مطالب را جست‌وجو کنید؛ بخشی از واژه را نیز می‌توانید بنویسید.',
    'Skip to article frontmatter': 'رفتن به مشخصات صفحه',
    'Skip to article content': 'رفتن به متن صفحه',
    'No results found.': 'نتیجه‌ای پیدا نشد.', 'No results found': 'نتیجه‌ای پیدا نشد', 'Close': 'بستن',
    'Search for a page': 'جست‌وجوی صفحه', 'Type to search...': 'برای جست‌وجو بنویسید…'
  });
  function hydrated(element) {
    const key = Object.keys(element).find(name => name.startsWith('__reactFiber'));
    return key && element[key]?.memoizedProps != null;
  }
  let scheduled = false;
  function sectionHash(route) {
    const labels = config.anchors?.[route] || [];
    const hash = decodeURIComponent(location.hash.slice(1));
    const visibleBand = Math.min(innerHeight * 0.6, 540);
    const anchored = labels.includes(hash) && document.getElementById(hash);
    // Keep an explicitly requested section through late font/image layout shifts.
    if (anchored) {
      const top = anchored.getBoundingClientRect().top;
      if (top >= -80 && top <= visibleBand) return '#' + encodeURIComponent(hash);
    }
    let current = null;
    let distance = Infinity;
    for (const id of labels) {
      const element = document.getElementById(id);
      if (!element) continue;
      const top = element.getBoundingClientRect().top;
      if (top <= visibleBand && Math.abs(top - 80) < distance) {
        current = id;
        distance = Math.abs(top - 80);
      }
    }
    if (current) return '#' + encodeURIComponent(current);
    return '';
  }
  function languageLinks(nav, route, paired) {
    for (const a of nav.querySelectorAll('[data-lang]')) {
      const target = a.dataset.lang;
      const suffix = paired ? (route ? route + '/' : '') + sectionHash(route) : 'translations/?from=' + encodeURIComponent(route);
      const href = config.base + (target === 'fa' ? '/fa/' : '/') + suffix;
      if (a.getAttribute('href') !== href) a.setAttribute('href', href);
      if (target === language) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      a.title = target === 'fa' && !paired ? 'ترجمهٔ این صفحه هنوز آماده نیست؛ وضعیت ترجمه‌ها' : target === 'fa' ? 'همین صفحه به فارسی' : 'This page in English';
    }
  }
  function localizeChrome() {
    // Explicit theme controls only: authored text and search excerpts are never roots.
    const roots = new Set(document.querySelectorAll([
      '.myst-search-bar', '.myst-top-nav-menu-button', '.myst-theme-button',
      '.myst-fm-downloads-button', '.myst-outline-collapsible', '.myst-outline-header',
      '.myst-skip-to-link', '.myst-made-with-myst',
      '.myst-primary-sidebar button', '.myst-primary-sidebar-toc button', '.myst-secondary-sidebar button',
      'button[aria-label="Copy code"]', 'button[aria-label="Copy to clipboard"]',
      '.myst-search-dialog input', '.myst-search-dialog label', '.myst-search-dialog button'
    ].join(',')));
    for (const dialog of document.querySelectorAll('.myst-search-dialog')) {
      for (const attr of ['aria-labelledby', 'aria-describedby']) {
        for (const id of (dialog.getAttribute(attr) || '').split(' ')) {
          const element = document.getElementById(id);
          if (element) roots.add(element);
        }
      }
      // Only the empty-state message, never a result, may be translated here.
      const results = dialog.querySelector('.myst-search-results');
      if (results && !results.querySelector('a,[role="option"]')) {
        for (const child of results.children) {
          if (['No results found.', 'No results found'].includes(child.textContent.trim())) roots.add(child);
        }
      }
    }
    for (const menu of document.querySelectorAll('[role="menu"]')) {
      const trigger = document.getElementById(menu.getAttribute('aria-labelledby'));
      if (trigger?.matches('.myst-theme-button')) roots.add(menu);
    }
    for (const element of roots) {
      if (!hydrated(element) || element.closest('.myst-search-results a,[role="option"],script,style')) continue;
      for (const attr of ['aria-label', 'title', 'placeholder']) {
        const value = element.getAttribute(attr);
        if (words[value]) element.setAttribute(attr, words[value]);
      }
      const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT);
      while (walker.nextNode()) {
        const node = walker.currentNode, parent = node.parentElement;
        if (!parent || parent.closest('script,style,code,pre,.katex,.myst-search-results a,[role="option"]') || !hydrated(parent)) continue;
        const key = node.textContent.trim();
        if (words[key]) node.textContent = node.textContent.replace(key, words[key]);
      }
    }
  }
  function update() {
    scheduled = false;
    const root = document.documentElement;
    if (root.lang !== language) root.lang = language;
    if (root.dir !== (fa ? 'rtl' : 'ltr')) root.dir = fa ? 'rtl' : 'ltr';
    let nav = document.getElementById('book-language-switcher');
    if (!nav) {
      const host = document.querySelector('.myst-top-nav-bar');
      if (!host) return;
      nav = document.createElement('nav');
      nav.id = 'book-language-switcher';
      nav.setAttribute('aria-label', fa ? 'زبان کتاب' : 'Book language');
      nav.innerHTML = '<a lang="en" dir="ltr" data-lang="en">English</a><span aria-hidden="true">|</span><a lang="fa" dir="rtl" data-lang="fa">فارسی</a>';
      host.append(nav);
    }
    const prefix = config.base + (fa ? '/fa' : '');
    // Static Pages adds a redirect for extensionless URLs without a final slash.
    // Normalize authored and sidebar links before a click or opening a new tab.
    for (const link of document.querySelectorAll('a[href]')) {
      const url = new URL(link.getAttribute('href'), location.href);
      if (url.origin !== location.origin || !url.pathname.startsWith(prefix + '/') || url.pathname.endsWith('/')) continue;
      const candidate = decodeURIComponent(url.pathname.slice(prefix.length)).replace(/^\/+|\/+$/g, '');
      if (config.routes.includes(candidate)) { url.pathname += '/';link.setAttribute('href', url.pathname + url.search + url.hash); }
    }
    const route = decodeURIComponent(location.pathname.slice(prefix.length)).replace(/^\/+|\/+$/g, '');
    const paired = config.routes.includes(route);
    languageLinks(nav, route, paired);
    if (!fa) return;
    // MyST's client links can drop the first segment of a nested BASE_URL.
    // Repair only this edition's /fa paths; external links retain their meaning.
    if (config.base) for (const el of document.querySelectorAll('a[href],img[src],iframe[src]')) {
      const attr = el.tagName === 'A' ? 'href' : 'src';
      const url = new URL(el.getAttribute(attr), location.href);
      if (url.origin === location.origin && (url.pathname === '/fa' || url.pathname.startsWith('/fa/'))) {
        el.setAttribute(attr, config.base + url.pathname + url.search + url.hash);
      }
    }
    localizeChrome();
    const source = new URLSearchParams(location.search).get('from');
    if (source && route === 'translations') {
      const target = document.getElementById('translation-request');
      if (target && !target.textContent) {
        target.textContent = 'ترجمهٔ صفحهٔ انتخاب‌شده هنوز منتشر نشده است: ' + source;
      }
    }
  }
  function enhance() {
    // A scroll/layout update must not change the destination during activation.
    // Capture the href the reader pressed, for both pointer and keyboard input.
    const activatedLinks = new WeakMap();
    const captureLanguageLink = event => {
      const link = event.target.closest?.('#book-language-switcher a[href]');
      if (link) activatedLinks.set(link, link.href);
    };
    window.addEventListener('pointerdown', captureLanguageLink, true);
    window.addEventListener('keydown', event => {
      if (event.key === 'Enter') captureLanguageLink(event);
    }, true);
    // Preserve the full nested GitHub Pages prefix across MyST link navigation.
    window.addEventListener('click', event => {
      const link = event.target.closest?.('a[href]');
      if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || link.download || link.target === '_blank') return;
      const url = new URL(activatedLinks.get(link) || link.href, location.href);
      activatedLinks.delete(link);
      if (fa && config.base && url.origin === location.origin && (url.pathname === '/fa' || url.pathname.startsWith('/fa/'))) url.pathname = config.base + url.pathname;
      if (url.origin !== location.origin || !url.pathname.startsWith(config.base + '/')) return;
      if (url.pathname === location.pathname && url.search === location.search) return;
      if (fa || link.closest('#book-language-switcher')) {
        // Use canonical directory URLs, including on local static servers.
        if (!url.pathname.endsWith('/') && !url.pathname.split('/').pop().includes('.')) url.pathname += '/';
        event.preventDefault();event.stopImmediatePropagation();location.assign(url.href);
      }
    }, true);
    new MutationObserver(() => {
      if (!scheduled) { scheduled = true; requestAnimationFrame(update); }
    }).observe(document.documentElement, {subtree: true, childList: true});
    for (const name of ['pushState','replaceState']) {
      const original = history[name];
      history[name] = function(...args) { const result = original.apply(this,args);requestAnimationFrame(update);return result; };
    }
    addEventListener('popstate', update);
    addEventListener('hashchange', update);
    let scrollScheduled = false;
    addEventListener('scroll', () => {
      if (scrollScheduled) return;
      scrollScheduled = true;
      requestAnimationFrame(() => {
        scrollScheduled = false;
        const prefix = config.base + (fa ? '/fa' : '');
        const route = decodeURIComponent(location.pathname.slice(prefix.length)).replace(/^\/+|\/+$/g, '');
        const nav = document.getElementById('book-language-switcher');
        if (nav) languageLinks(nav, route, config.routes.includes(route));
      });
    }, {passive: true});
    update();
    setTimeout(update, 1000);
    setTimeout(update, 3000);
  }
  function ready() {
    // React attaches its fiber marker when this header has hydrated.
    const header = document.querySelector('.myst-top-nav-bar');
    if (!header || !hydrated(header)) {
      setTimeout(ready, 50);return;
    }
    enhance();
  }
  // A header fiber can exist before the rest of the document has hydrated.
  // Keep the verified load grace period; early DOM edits cause React #418.
  if (document.readyState === 'complete') setTimeout(ready, 300);
  else addEventListener('load', () => setTimeout(ready, 300), {once: true});
})();
