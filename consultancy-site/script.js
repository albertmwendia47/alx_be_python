(function () {
  const navToggleButton = document.getElementById('navToggle');
  const siteNav = document.getElementById('siteNav');

  function toggleNav() {
    const isOpen = siteNav.classList.toggle('open');
    navToggleButton.setAttribute('aria-expanded', String(isOpen));
  }

  if (navToggleButton && siteNav) {
    navToggleButton.addEventListener('click', toggleNav);
  }

  // Close nav on link click (mobile)
  siteNav?.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      siteNav.classList.remove('open');
      navToggleButton?.setAttribute('aria-expanded', 'false');
    });
  });

  // Smooth scrolling for on-page anchors
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const targetId = anchor.getAttribute('href');
      if (!targetId || targetId.length <= 1) return;
      const target = document.querySelector(targetId);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // Update year in footer
  const yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }
})();