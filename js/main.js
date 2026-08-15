/* =============================================
   CAP SUR VALENCIA - JavaScript Principal
   Design v4 Senior / Awwwards
   Progressive Enhancement & IntersectionObserver
   ============================================= */

// --- Scroll Animations (IntersectionObserver) ---
const observerOptions = {
  root: null,
  rootMargin: '0px 0px -40px 0px',
  threshold: 0.08
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

// --- Top Sentinel Observer (Navbar Scrolled + Back To Top) ---
// Rule 3: Zero window.addEventListener('scroll') - IntersectionObserver only!
function initTopObserver() {
  const navbar = document.querySelector('.navbar');
  const backToTopBtn = document.getElementById('back-to-top') || document.querySelector('.back-to-top');

  let topSentinel = document.getElementById('top-sentinel');
  if (!topSentinel) {
    topSentinel = document.createElement('div');
    topSentinel.id = 'top-sentinel';
    topSentinel.setAttribute('aria-hidden', 'true');
    topSentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:60px;pointer-events:none;';
    document.body.prepend(topSentinel);
  }

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (navbar) {
        if (!entry.isIntersecting) {
          navbar.classList.add('scrolled');
        } else {
          navbar.classList.remove('scrolled');
        }
      }
      if (backToTopBtn) {
        if (!entry.isIntersecting) {
          backToTopBtn.classList.add('visible');
        } else {
          backToTopBtn.classList.remove('visible');
        }
      }
    });
  }, {
    rootMargin: '0px 0px 0px 0px',
    threshold: 0
  });

  navObserver.observe(topSentinel);
}

// --- Back to Top Click Handler ---
function initBackToTop() {
  const backToTopBtn = document.getElementById('back-to-top') || document.querySelector('.back-to-top');
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
}

// --- Mobile Navigation ---
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');
const navOverlay = document.querySelector('.nav-overlay');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('open');
    navLinks.classList.toggle('open');
    if (navOverlay) navOverlay.classList.toggle('open');
    document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
  });

  if (navOverlay) {
    navOverlay.addEventListener('click', () => {
      navToggle.classList.remove('open');
      navLinks.classList.remove('open');
      navOverlay.classList.remove('open');
      document.body.style.overflow = '';
    });
  }

  // Close nav on link click
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('open');
      navLinks.classList.remove('open');
      if (navOverlay) navOverlay.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}

// --- Smooth Counter Animation ---
function animateCounter(el, target, duration = 2000) {
  const start = 0;
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    // Ease-out
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(start + (target - start) * eased);

    el.textContent = current.toLocaleString();

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      el.textContent = target.toLocaleString();
    }
  }

  requestAnimationFrame(update);
}

// Animate counters when visible
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      if (target) {
        animateCounter(el, target);
        counterObserver.unobserve(el);
      }
    }
  });
}, { threshold: 0.5 });

// --- Countdown Timer ---
function updateCountdown() {
  const targetDate = new Date('2028-06-01T00:00:00+02:00');
  const now = new Date();
  const diff = targetDate - now;

  if (diff <= 0) {
    document.querySelectorAll('.countdown-value.days').forEach(el => { el.textContent = '0'; });
    return;
  }

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const months = Math.floor(days / 30);
  const remainingDays = days % 30;

  const monthEls = document.querySelectorAll('.countdown-value.months');
  const dayEls = document.querySelectorAll('.countdown-value.days-remaining');

  monthEls.forEach(el => { el.textContent = months; });
  dayEls.forEach(el => { el.textContent = remainingDays; });
}

// --- Budget Calculator ---
function initBudgetCalculator() {
  const scenarioBtns = document.querySelectorAll('.calc-scenario button');
  if (!scenarioBtns.length) return;

  const scenarios = {
    sobre: {
      loyer: 950, charges: 155, internet: 45, courses: 600,
      transports: 90, cantine: 270, activites: 150, mutuelle: 0,
      restos: 100, divers: 120
    },
    confort: {
      loyer: 1200, charges: 215, internet: 55, courses: 700,
      transports: 100, cantine: 360, activites: 220, mutuelle: 200,
      restos: 200, divers: 175
    },
    tranquille: {
      loyer: 1500, charges: 275, internet: 65, courses: 800,
      transports: 110, cantine: 450, activites: 300, mutuelle: 250,
      restos: 400, divers: 285
    }
  };

  function updateCalculator(scenario) {
    const data = scenarios[scenario];

    const map = {
      'calc-loyer': data.loyer,
      'calc-charges': data.charges,
      'calc-internet': data.internet,
      'calc-courses': data.courses,
      'calc-transports': data.transports,
      'calc-cantine': data.cantine,
      'calc-activites': data.activites,
      'calc-mutuelle': data.mutuelle,
      'calc-restos': data.restos,
      'calc-divers': data.divers
    };

    let total = 0;
    for (const [id, value] of Object.entries(map)) {
      const el = document.getElementById(id);
      if (el) {
        el.textContent = value.toLocaleString() + ' €';
        total += value;
      }
    }

    const totalEl = document.getElementById('calc-total');
    if (totalEl) {
      totalEl.textContent = total.toLocaleString() + ' €';
      // Animate
      totalEl.style.transform = 'scale(1.08)';
      setTimeout(() => { totalEl.style.transform = 'scale(1)'; }, 150);
    }
  }

  scenarioBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      scenarioBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateCalculator(btn.dataset.scenario);
    });
  });

  // Initialize with "confort"
  updateCalculator('confort');
}

// --- Quartier Filter ---
function initQuartierFilter() {
  const filterBtns = document.querySelectorAll('.quartier-filter button');
  const cards = document.querySelectorAll('.quartier-card');

  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;

      cards.forEach(card => {
        if (filter === 'all' || card.dataset.category === filter) {
          card.style.display = 'block';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 50);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => { card.style.display = 'none'; }, 300);
        }
      });

      cards.forEach(card => {
        card.style.transition = 'all 0.3s ease';
      });
    });
  });
}

// --- Budget Sticky Subnav Spy ---
function initBudgetSubnavSpy() {
  const chips = document.querySelectorAll('.budget-subnav-chip');
  if (!chips.length) return;

  const sectionIds = ['loyer', 'manger-dehors', 'scenarios', 'installation', 'salaires', 'restos'];
  const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
  if (!sections.length) return;

  const spyObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        chips.forEach(chip => {
          if (chip.getAttribute('href') === '#' + id) {
            chip.classList.add('active');
          } else {
            chip.classList.remove('active');
          }
        });
      }
    });
  }, {
    rootMargin: '-80px 0px -55% 0px',
    threshold: 0.1
  });

  sections.forEach(sec => spyObserver.observe(sec));
}

// --- Checklists LocalStorage Persistence ---
function initChecklists() {
  const checkboxes = document.querySelectorAll('.checklist-checkbox');
  if (!checkboxes.length) return;

  const storageKey = 'cap_valencia_checklists';
  let savedState = {};
  try {
    const raw = localStorage.getItem(storageKey);
    if (raw) savedState = JSON.parse(raw);
  } catch (e) {
    console.error('LocalStorage unavailable for checklists', e);
  }

  checkboxes.forEach((chk, index) => {
    const id = chk.id || `chk_${index}`;
    if (!chk.id) chk.id = id;

    // Restore state
    if (savedState[id]) {
      chk.checked = true;
      const parent = chk.closest('.checklist-item');
      if (parent) parent.classList.add('checked');
    }

    chk.addEventListener('change', () => {
      savedState[id] = chk.checked;
      const parent = chk.closest('.checklist-item');
      if (parent) {
        if (chk.checked) parent.classList.add('checked');
        else parent.classList.remove('checked');
      }
      try {
        localStorage.setItem(storageKey, JSON.stringify(savedState));
      } catch (e) {
        console.error('Failed to save checklist state', e);
      }
    });
  });
}

// --- Reading Progress Fallback for Browsers without CSS scroll-timeline ---
function initReadingProgressFallback() {
  const progressBar = document.querySelector('.reading-progress');
  if (!progressBar) return;

  // If CSS animation-timeline is supported, CSS handles it directly
  if (CSS.supports && CSS.supports('animation-timeline', 'scroll()')) {
    return;
  }

  // Fallback: observe document sections to step progress
  const allSections = document.querySelectorAll('section, main, header, footer');
  if (!allSections.length) return;

  const total = allSections.length;
  let seen = new Set();

  const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        seen.add(entry.target);
        const ratio = seen.size / total;
        progressBar.style.transform = `scaleX(${Math.min(ratio, 1)})`;
      }
    });
  }, { threshold: 0.1 });

  allSections.forEach(sec => progressObserver.observe(sec));
}

// --- Initialize Everything ---
document.addEventListener('DOMContentLoaded', () => {
  initTopObserver();
  initBackToTop();
  initBudgetCalculator();
  initQuartierFilter();
  initBudgetSubnavSpy();
  initChecklists();
  initReadingProgressFallback();

  updateCountdown();
  setInterval(updateCountdown, 1000 * 60 * 60); // Every hour

  document.querySelectorAll('.hero-stat-value[data-target]').forEach(el => counterObserver.observe(el));

  // Add fade-in class and observe
  document.querySelectorAll('.section > *, .card, .quartier-card, .blog-card, .pull-quote, .section-pause-editorial').forEach(el => {
    if (!el.classList.contains('fade-in')) {
      el.classList.add('fade-in');
    }
    observer.observe(el);
  });
});
