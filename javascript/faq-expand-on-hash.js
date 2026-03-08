(function () {
  function openDetailsAfter(el) {
    if (!el) return;
    var next = el.nextElementSibling;
    while (next) {
      var details = next.tagName === 'DETAILS' ? next : next.querySelector('details');
      if (details) {
        details.open = true;
        return true;
      }
      next = next.nextElementSibling;
    }
    /* If not found as next sibling, try parent's next sibling (e.g. wrapper divs) */
    var parent = el.parentElement;
    if (parent && parent.nextElementSibling) {
      var wrapper = parent.nextElementSibling;
      var d = wrapper.tagName === 'DETAILS' ? wrapper : wrapper.querySelector('details');
      if (d) {
        d.open = true;
        return true;
      }
    }
    return false;
  }

  function expandFaqForId(id) {
    if (!id) return;
    var target = document.getElementById(id);
    if (target) openDetailsAfter(target);
  }

  function expandFaqFromHash() {
    var hash = window.location.hash;
    if (!hash || hash === '#') return;
    var id = hash.slice(1).split('?')[0];
    expandFaqForId(id);
  }

  function getIdFromHref(href) {
    if (!href || typeof href !== 'string') return null;
    var i = href.indexOf('#');
    if (i === -1) return null;
    return href.slice(i + 1).split('?')[0].trim() || null;
  }

  /* Get the id of the heading that precedes this details (for URL fragment) */
  function getHeadingIdForDetails(details) {
    if (!details || details.tagName !== 'DETAILS') return null;
    var el = details.previousElementSibling;
    while (el) {
      if (el.id) return el.id;
      el = el.previousElementSibling;
    }
    var parent = details.parentElement;
    if (parent && parent.previousElementSibling && parent.previousElementSibling.id) {
      return parent.previousElementSibling.id;
    }
    return null;
  }

  function isFaqPage() {
    return document.querySelector('.faq-question') !== null;
  }

  function updateFragmentOnDetailsToggle(e) {
    if (!isFaqPage()) return;
    var details = e.target;
    if (details.tagName !== 'DETAILS') return;
    var path = window.location.pathname + (window.location.search || '');
    if (details.open) {
      var id = getHeadingIdForDetails(details);
      if (id) history.replaceState(null, '', path + '#' + id);
    } else {
      history.replaceState(null, '', path);
    }
  }

  window.addEventListener('load', function () {
    expandFaqFromHash();
  });
  window.addEventListener('hashchange', expandFaqFromHash);

  /* Click: use capture so we run before Material; handle any link that has a hash */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="#"]');
    if (!a) return;
    var id = getIdFromHref(a.getAttribute('href'));
    if (!id) return;
    /* Run after a short delay so target is in DOM and scroll has been applied */
    setTimeout(function () {
      expandFaqForId(id);
    }, 50);
  }, true);

  /* Update URL fragment when user expands/collapses an FAQ section */
  document.addEventListener('toggle', updateFragmentOnDetailsToggle, true);
})();
