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
    'Open Folder': 'باز کردن بخش', 'Close Folder': 'بستن بخش',
    'Toggle theme between light and dark mode': 'تغییر ظاهر روشن و تیره',
    'CONTENTS': 'فهرست این صفحه', 'Search Website': 'جست‌وجو در کتاب',
    'Search articles and their contents using fuzzy-search and prefix-matching': 'عنوان و متن مطالب را جست‌وجو کنید؛ بخشی از واژه را نیز می‌توانید بنویسید.',
    'Skip to article frontmatter': 'رفتن به مشخصات صفحه',
    'Skip to article content': 'رفتن به متن صفحه',
    'No results found.': 'نتیجه‌ای پیدا نشد.', 'No results found': 'نتیجه‌ای پیدا نشد',
    'Search for a page': 'جست‌وجوی صفحه', 'Type to search...': 'برای جست‌وجو بنویسید…'
  });
  let scheduled = false;
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
    const route = decodeURIComponent(location.pathname.slice(prefix.length)).replace(/^\/+|\/+$/g, '');
    const paired = config.routes.includes(route);
    for (const a of nav.querySelectorAll('[data-lang]')) {
      const target = a.dataset.lang;
      const suffix = paired ? (route ? route + '/' : '') : 'translations/?from=' + encodeURIComponent(route);
      const href = config.base + (target === 'fa' ? '/fa/' : '/') + suffix;
      if (a.getAttribute('href') !== href) a.setAttribute('href', href);
      if (target === language) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      a.title = target === 'fa' && !paired ? 'ترجمهٔ این صفحه هنوز آماده نیست؛ وضعیت ترجمه‌ها' : target === 'fa' ? 'همین صفحه به فارسی' : 'This page in English';
    }
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
    // Only theme chrome is localized here. Authored Persian content is in source files.
    for (const el of document.querySelectorAll('nav,button,aside,header,[role="dialog"],input')) {
      for (const attr of ['aria-label', 'title', 'placeholder']) {
        const val = el.getAttribute(attr);
        if (words[val]) el.setAttribute(attr, words[val]);
      }
      if (el.closest('article')) continue;
    }
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    while (walker.nextNode()) {
      const node = walker.currentNode, parent = node.parentElement;
      if (!parent || parent.closest('script,style,code,pre,.katex')) continue;
      const key = node.textContent.trim();
      if (words[key]) node.textContent = node.textContent.replace(key, words[key]);
    }
    const source = new URLSearchParams(location.search).get('from');
    if (source && route === 'translations') {
      const target = document.getElementById('translation-request');
      if (target && !target.textContent) {
        target.textContent = 'ترجمهٔ صفحهٔ انتخاب‌شده هنوز منتشر نشده است: ' + source;
      }
    }
  }
  function enhance() {
    // Preserve the full nested GitHub Pages prefix across MyST link navigation.
    window.addEventListener('click', event => {
      const link = event.target.closest?.('a[href]');
      if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || link.download || link.target === '_blank') return;
      const url = new URL(link.href, location.href);
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
    update();
  }
  function ready() {
    // React attaches its fiber marker when this header has hydrated.
    const header = document.querySelector('.myst-top-nav-bar');
    if (!header || !Object.keys(header).some(key => key.startsWith('__reactFiber'))) {
      setTimeout(ready, 100);return;
    }
    enhance();
  }
  if (document.readyState === 'complete') setTimeout(ready, 300);
  else addEventListener('load', () => setTimeout(ready, 300), {once: true});
})();
