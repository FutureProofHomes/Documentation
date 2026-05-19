(() => {
  function syncToc() {
    var tabbedSets = document.querySelectorAll('.tabbed-set');
    if (!tabbedSets.length) return;

    var hiddenIds = new Set();

    tabbedSets.forEach(function(set) {
      var inputs = Array.from(set.querySelectorAll(':scope > input[type="radio"]'));
      var blocks = Array.from(
        set.querySelectorAll(':scope > .tabbed-content > .tabbed-block')
      );

      inputs.forEach(function(input, idx) {
        var block = blocks[idx];
        if (!block) return;
        if (!input.checked) {
          block.querySelectorAll('[id]').forEach(function(el) {
            hiddenIds.add(el.id);
          });
        }
      });
    });

    if (!hiddenIds.size) return;

    document.querySelectorAll('.md-nav a[href*="#"]').forEach(function(link) {
      var href = link.getAttribute('href');
      if (!href) return;
      var hashIdx = href.indexOf('#');
      if (hashIdx === -1) return;
      var id = href.slice(hashIdx + 1);
      var li = link.closest('li');
      if (!li) return;
      if (hiddenIds.has(id)) {
        li.classList.add('toc-tab-hidden');
      } else {
        li.classList.remove('toc-tab-hidden');
      }
    });
  }

  function init() {
    syncToc();
    document.addEventListener('change', function(e) {
      if (e.target && e.target.name && e.target.name.indexOf('__tabbed') === 0) {
        requestAnimationFrame(syncToc);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  document.addEventListener('DOMContentLoaded', function() {
    if (window.document$) {
      window.document$.subscribe(function() {
        setTimeout(syncToc, 50);
      });
    }
  });
})();
