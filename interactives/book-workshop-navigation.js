(() => {
  'use strict';
  const fa = document.currentScript.dataset.language === 'fa';
  const outlineLabel = fa ? 'فهرست' : 'Contents';
  const expandLabel = fa ? 'باز کردن فهرست این صفحه' : 'Show page contents';
  const collapseLabel = fa ? 'بستن فهرست این صفحه' : 'Hide page contents';
  const frameSelector = '.chapter03-workshop-frame iframe';
  const sectionSelector = '.workshop-page-outline a[href^="#"]';
  let frame, contents, sections = [], active = '';
  let resizeObserver, queuedScroll = 0;

  function highlight() {
    for (const link of document.querySelectorAll(sectionSelector)) {
      if (link.hash === active) {
        if (!link.hasAttribute('aria-current')) link.setAttribute('aria-current', 'location');
      } else if (link.hasAttribute('aria-current')) {
        link.removeAttribute('aria-current');
      }
    }
  }


  function buildOutline() {
    const side = frame.closest('article').querySelector(':scope > div.lg\\:col-margin-right');
    if (!side || side.querySelector('.workshop-page-outline')) return;
    const panel = document.createElement('div');
    panel.className = 'myst-outline-section workshop-page-outline';
    const nav = document.createElement('nav');
    nav.className = 'myst-outline not-prose overflow-y-auto rounded-lg';
    nav.setAttribute('aria-label', outlineLabel);

    const header = document.createElement('div');
    header.className = 'myst-outline-header flex flex-row gap-2 text-sm leading-6';
    header.append(outlineLabel);

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'myst-outline-collapsible';
    toggle.setAttribute('aria-controls', 'workshop-outline-items');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', collapseLabel);
    toggle.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true" width="24" height="24"><path d="m9 6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    header.append(toggle);
    const list = document.createElement('ul');
    list.id = 'workshop-outline-items';
    list.className = 'myst-outline-list text-sm leading-6';
    for (const [index, section] of sections.slice(1).entries()) {
      const sourceLink = [...contents.querySelectorAll('#rail nav a')].find(link => link.hash === '#' + section.id);
      const name = sourceLink.querySelector('span:last-child').textContent;
      const number = '3.7.' + (index + 1);
      const link = document.createElement('a');
      link.href = '#' + section.id;
      link.textContent = (fa ? number.replace(/[0-9]/g, digit => '۰۱۲۳۴۵۶۷۸۹'[Number(digit)]) : number) + ' ' + name;
      link.className = 'block p-1 text-myst-text pr-2 pl-2';
      const item = document.createElement('li');
      item.className = 'myst-outline-item';
      item.append(link);
      list.append(item);
    }
    toggle.addEventListener('click', () => {
      list.hidden = !list.hidden;
      toggle.setAttribute('aria-expanded', String(!list.hidden));
      toggle.setAttribute('aria-label', list.hidden ? expandLabel : collapseLabel);
    });
    nav.append(header,list);
    panel.append(nav);
    side.append(panel);
  }

  function scrollToSection(section) {
    const masthead = document.querySelector('.myst-top-nav')?.getBoundingClientRect().height || 64;
    const outerTop = frame.getBoundingClientRect().top;
    const innerTop = section.getBoundingClientRect().top;
    window.scrollTo({top: window.scrollY + outerTop + innerTop - masthead - 15});
  }

  function reveal(hash) {
    const section = sections.find(section => '#' + section.id === hash);
    if (!section) return;
    scrollToSection(section);
    section.querySelector('h1,h2')?.focus({preventScroll:true});
    active = hash;
    highlight();
  }

  function fit() {
    if (!contents?.body) return;
    const requested = Math.ceil(contents.body.getBoundingClientRect().height);
    if (requested < 1) return;
    const height = requested + 'px';
    if (frame.parentElement.style.height !== height) frame.parentElement.style.height = height;
  }

  function syncScroll() {
    queuedScroll = 0;
    if (!frame?.isConnected || !sections.length) return;
    const edge = 100 - frame.getBoundingClientRect().top;
    let visible = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= edge) visible = section;
      else break;
    }
    const hash = '#' + visible.id;
    if (hash !== active) {
      active = hash;
      highlight();
    }
  }

  function jump(hash) {
    if (location.hash !== hash) history.pushState(history.state, '', hash);
    reveal(hash);
  }

  function bind(workshop) {
    frame = workshop;
    function ready() {
      contents = frame.contentDocument;
      const rail = contents?.getElementById('rail');
      if (!rail || rail.dataset.mergedIntoBook) return;
      rail.dataset.mergedIntoBook = 'true';
      sections = [...rail.querySelectorAll('nav a[href^="#"]')].map(link => contents.getElementById(link.hash.slice(1))).filter(Boolean);
      buildOutline();
      resizeObserver?.disconnect();
      resizeObserver = new ResizeObserver(fit);
      resizeObserver.observe(contents.body);
      fit();
      if (location.hash) requestAnimationFrame(() => reveal(location.hash));
      else syncScroll();
    }
    workshop.addEventListener('load', ready);
    if (workshop.contentDocument?.readyState === 'complete') ready();
  }

  window.addEventListener('click', event => {
    const link = event.target.closest?.(sectionSelector);
    if (!link || event.defaultPrevented || event.button !== 0 ||
        event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    event.stopImmediatePropagation();
    jump(link.hash);
  }, true);
  window.addEventListener('hashchange', () => reveal(location.hash || '#overview'));
  window.addEventListener('scroll', () => {
    if (!queuedScroll) queuedScroll = requestAnimationFrame(syncScroll);
  }, {passive:true});
  window.addEventListener('resize', () => { fit(); syncScroll(); }, {passive:true});

  let hydrationCheck = 0;
  function refresh() {
    const workshop = document.querySelector(frameSelector);
    if (workshop && workshop !== frame) {
      const fiber = Object.keys(workshop).find(key => key.startsWith('__reactFiber'));
      if (fiber && workshop[fiber]?.memoizedProps) {
        bind(workshop);
      } else if (!hydrationCheck) {
        hydrationCheck = requestAnimationFrame(() => {
          hydrationCheck = 0;
          refresh();
        });
      }
    }
    highlight();
  }
  new MutationObserver(refresh).observe(document.body, {subtree: true, childList: true});
  refresh();
})();
