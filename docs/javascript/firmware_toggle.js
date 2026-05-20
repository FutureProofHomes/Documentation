(() => {
  var STORAGE_KEY = "fph-firmware-mode";
  var MODES = ["stable", "beta"];

  var SUN_SVG =
    '<svg class="theme-toggle__icon theme-toggle__sun" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">' +
    '<circle cx="12" cy="12" r="5" fill="currentColor"/>' +
    '<g stroke="currentColor" stroke-width="2" stroke-linecap="round">' +
    '<line x1="12" y1="1" x2="12" y2="3"/>' +
    '<line x1="12" y1="21" x2="12" y2="23"/>' +
    '<line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>' +
    '<line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>' +
    '<line x1="1" y1="12" x2="3" y2="12"/>' +
    '<line x1="21" y1="12" x2="23" y2="12"/>' +
    '<line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>' +
    '<line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>' +
    "</g></svg>";

  var MOON_SVG =
    '<svg class="theme-toggle__icon theme-toggle__moon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">' +
    '<path fill="currentColor" d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>' +
    "</svg>";

  // ── Firmware mode helpers ──

  function getMode() {
    var stored = localStorage.getItem(STORAGE_KEY);
    return MODES.indexOf(stored) !== -1 ? stored : "stable";
  }

  function setMode(mode) {
    localStorage.setItem(STORAGE_KEY, mode);
    activateTabs(mode);
    updateToggleUI(mode);
    updateBanner(mode);
    updateModeVisibility(mode);
  }

  function activateTabs(mode) {
    var label = mode === "beta" ? "Beta" : "Stable";
    document.querySelectorAll(".tabbed-set").forEach(function (set) {
      var labels = set.querySelectorAll(":scope > .tabbed-labels > label");
      labels.forEach(function (lbl) {
        if (lbl.textContent.trim() === label) {
          lbl.click();
        }
      });
    });
  }

  function updateToggleUI(mode) {
    var toggle = document.getElementById("fw-toggle");
    if (!toggle) return;
    toggle.querySelectorAll("button").forEach(function (btn) {
      var isActive = btn.dataset.mode === mode;
      btn.classList.toggle("fw-toggle__btn--active", isActive);
      btn.setAttribute("aria-pressed", String(isActive));
      btn.setAttribute("aria-checked", String(isActive));
    });
    toggle.dataset.active = mode;
  }

  function updateBanner(mode) {
    var banner = document.getElementById("beta-banner");
    if (banner) {
      banner.style.display = mode === "beta" ? "flex" : "none";
    }
  }

  function updateModeVisibility(mode) {
    document.querySelectorAll(".stable-only").forEach(function (el) {
      el.style.display = mode === "stable" ? "" : "none";
    });
    document.querySelectorAll(".beta-only").forEach(function (el) {
      el.style.display = mode === "beta" ? "" : "none";
    });
  }

  // ── Firmware toggle (segmented control in sidebar) ──

  function findSatelliteNav() {
    var sidebar = document.querySelector(".md-sidebar--primary");
    if (!sidebar) return null;

    var els = sidebar.querySelectorAll(".md-nav__link, .md-nav__title");
    for (var i = 0; i < els.length; i++) {
      if (els[i].textContent.trim() === "Satellite1 Dev Kit") {
        var item = els[i].closest(".md-nav__item");
        if (item) {
          return item.querySelector(":scope > .md-nav > ul");
        }
        var nav = els[i].closest(".md-nav");
        if (nav) {
          return nav.querySelector(":scope > ul");
        }
      }
    }
    return null;
  }

  function createFirmwareToggle() {
    var existing = document.getElementById("fw-toggle");
    if (existing) existing.closest(".fw-toggle-li").remove();

    var navList = findSatelliteNav();
    if (!navList) return;

    var wrapper = document.createElement("div");
    wrapper.id = "fw-toggle";
    wrapper.className = "fw-toggle";
    wrapper.setAttribute("role", "radiogroup");
    wrapper.setAttribute("aria-label", "Firmware documentation version");

    var mode = getMode();
    wrapper.dataset.active = mode;

    MODES.forEach(function (m) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "fw-toggle__btn";
      btn.dataset.mode = m;
      btn.textContent = m.charAt(0).toUpperCase() + m.slice(1);
      btn.setAttribute("role", "radio");
      btn.setAttribute("aria-checked", String(m === mode));
      if (m === mode) {
        btn.classList.add("fw-toggle__btn--active");
        btn.setAttribute("aria-pressed", "true");
      } else {
        btn.setAttribute("aria-pressed", "false");
      }
      btn.addEventListener("click", function () {
        setMode(m);
      });
      wrapper.appendChild(btn);
    });

    var li = document.createElement("li");
    li.className = "md-nav__item fw-toggle-li";
    li.appendChild(wrapper);
    navList.appendChild(li);
  }

  // ── Theme toggle (dark / light pill switch) ──

  function createThemeToggle() {
    if (document.getElementById("theme-toggle")) return;

    var btn = document.createElement("button");
    btn.id = "theme-toggle";
    btn.className = "theme-toggle";
    btn.type = "button";
    btn.setAttribute("aria-label", "Toggle dark mode");

    var thumb = document.createElement("span");
    thumb.className = "theme-toggle__thumb";
    thumb.innerHTML = SUN_SVG + MOON_SVG;
    btn.appendChild(thumb);

    btn.addEventListener("click", function () {
      var toggle = document.querySelector(
        'input[data-md-toggle="palette"]'
      );
      if (toggle) {
        toggle.click();
        return;
      }
      var cb = document.getElementById("__palette");
      if (cb) {
        cb.click();
        return;
      }
      var label = document.querySelector(
        '[data-md-component="palette"] label:not([hidden])'
      );
      if (label) label.click();
    });

    var header = document.querySelector(".md-header__inner.md-grid");
    if (!header) return;
    var ref = header.querySelector(".md-search");
    if (ref) {
      header.insertBefore(btn, ref);
    } else {
      header.appendChild(btn);
    }
  }

  // ── Sync header when a content tab is clicked directly ──

  var _syncing = false;

  function onContentTabChange(e) {
    if (_syncing) return;
    if (!e.target || !e.target.name || e.target.name.indexOf("__tabbed") !== 0)
      return;
    var input = e.target;
    var set = input.closest(".tabbed-set");
    if (!set) return;
    var inputs = Array.from(set.querySelectorAll(':scope > input[type="radio"]'));
    var idx = inputs.indexOf(input);
    var labels = set.querySelectorAll(":scope > .tabbed-labels > label");
    var label = labels[idx];
    if (!label) return;
    var text = label.textContent.trim().toLowerCase();
    if (MODES.indexOf(text) === -1) return;
    if (text === getMode()) return;
    _syncing = true;
    localStorage.setItem(STORAGE_KEY, text);
    updateToggleUI(text);
    updateBanner(text);
    _syncing = false;
  }

  // ── Initialization ──

  function syncOnPageLoad() {
    createFirmwareToggle();
    var mode = getMode();
    _syncing = true;
    setTimeout(function () {
      activateTabs(mode);
      updateToggleUI(mode);
      updateBanner(mode);
      updateModeVisibility(mode);
      _syncing = false;
    }, 60);
  }

  function init() {
    createFirmwareToggle();
    createThemeToggle();
    document.addEventListener("change", onContentTabChange);
    syncOnPageLoad();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (window.document$) {
      window.document$.subscribe(function () {
        syncOnPageLoad();
      });
    }
  });
})();
