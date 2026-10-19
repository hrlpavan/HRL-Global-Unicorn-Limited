/**
 * HRL X MacOS 27 V2.0 - Interactive Desktop Controller
 * Implements Parabolic Dock Magnification, Window Chrome, Control Center, Spotlight
 */

document.addEventListener('DOMContentLoaded', () => {
  initClock();
  initDropdowns();
  initControlCenter();
  initSpotlight();
  initDockMagnification();
  initWindowControls();
  initThemeToggle();
});

/* ========================================================= */
/* 1. LIVE MENU BAR CLOCK                                    */
/* ========================================================= */
function initClock() {
  const clockEl = document.getElementById('menubarClock');
  if (!clockEl) return;

  function update() {
    const now = new Date();
    const options = { 
      weekday: 'short', 
      month: 'short', 
      day: 'numeric', 
      hour: 'numeric', 
      minute: '2-digit',
      hour12: true 
    };
    clockEl.textContent = now.toLocaleString('en-US', options).replace(/,/g, '');
  }
  update();
  setInterval(update, 1000);
}

/* ========================================================= */
/* 2. MENU BAR DROPDOWNS                                     */
/* ========================================================= */
function initDropdowns() {
  const triggers = document.querySelectorAll('[data-menu-target]');
  
  triggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const menuId = trigger.getAttribute('data-menu-target');
      const targetMenu = document.getElementById(menuId);
      
      // Close other open menus
      document.querySelectorAll('.apple-dropdown-menu').forEach(menu => {
        if (menu !== targetMenu) menu.classList.remove('show');
      });

      if (targetMenu) {
        targetMenu.classList.toggle('show');
        // Align dropdown under trigger
        const rect = trigger.getBoundingClientRect();
        targetMenu.style.left = `${rect.left}px`;
      }
    });
  });

  // Global click outside to dismiss
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.apple-dropdown-menu') && !e.target.closest('[data-menu-target]')) {
      document.querySelectorAll('.apple-dropdown-menu').forEach(m => m.classList.remove('show'));
    }
  });
}

/* ========================================================= */
/* 3. CONTROL CENTER TOGGLE                                  */
/* ========================================================= */
function initControlCenter() {
  const ccBtn = document.getElementById('controlCenterBtn');
  const ccPopup = document.getElementById('controlCenterPopup');
  
  if (ccBtn && ccPopup) {
    ccBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      ccPopup.classList.toggle('show');
    });

    document.addEventListener('click', (e) => {
      if (!ccPopup.contains(e.target) && !ccBtn.contains(e.target)) {
        ccPopup.classList.remove('show');
      }
    });
  }

  // Interactive CC Toggle Buttons
  document.querySelectorAll('.cc-card').forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('active');
    });
  });
}

/* ========================================================= */
/* 4. SPOTLIGHT SEARCH (⌘ + Space)                           */
/* ========================================================= */
function initSpotlight() {
  const spotlightBtn = document.getElementById('spotlightBtn');
  const spotlightModal = document.getElementById('spotlightModal');
  const spotlightInput = document.getElementById('spotlightInput');
  const resultsContainer = document.getElementById('spotlightResults');

  if (!spotlightModal) return;

  function toggleSpotlight() {
    spotlightModal.classList.toggle('show');
    if (spotlightModal.classList.contains('show')) {
      setTimeout(() => spotlightInput && spotlightInput.focus(), 50);
    }
  }

  if (spotlightBtn) {
    spotlightBtn.addEventListener('click', toggleSpotlight);
  }

  // Global Keyboard shortcut: Command+Space or Ctrl+Space or Escape to close
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.code === 'Space') {
      e.preventDefault();
      toggleSpotlight();
    }
    if (e.key === 'Escape' && spotlightModal.classList.contains('show')) {
      spotlightModal.classList.remove('show');
    }
  });

  // Search Filter
  if (spotlightInput && resultsContainer) {
    const items = resultsContainer.querySelectorAll('.spotlight-result-item');
    spotlightInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      items.forEach(item => {
        const text = item.textContent.toLowerCase();
        item.style.display = text.includes(q) ? 'flex' : 'none';
      });
    });
  }
}

/* ========================================================= */
/* 5. PARABOLIC APPLE DOCK MAGNIFICATION                     */
/* ========================================================= */
function initDockMagnification() {
  const dock = document.querySelector('.macos-dock');
  if (!dock) return;

  const items = dock.querySelectorAll('.dock-item');
  const baseSize = 38;
  const maxScale = 1.55;
  const range = 95; // Pixel radius of magnification influence

  dock.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX;

    items.forEach(item => {
      const rect = item.getBoundingClientRect();
      const itemCenterX = rect.left + rect.width / 2;
      const distance = Math.abs(mouseX - itemCenterX);

      if (distance < range) {
        // Smooth cosine bell-curve magnification
        const factor = Math.cos((distance / range) * (Math.PI / 2));
        const scale = 1 + (maxScale - 1) * Math.pow(factor, 1.4);
        const newSize = Math.round(baseSize * scale);
        item.style.width = `${newSize}px`;
        item.style.height = `${newSize}px`;
        item.style.transform = `translateY(-${Math.round((scale - 1) * 20)}px)`;
      } else {
        item.style.width = `${baseSize}px`;
        item.style.height = `${baseSize}px`;
        item.style.transform = 'translateY(0)';
      }
    });
  });

  dock.addEventListener('mouseleave', () => {
    items.forEach(item => {
      item.style.width = `${baseSize}px`;
      item.style.height = `${baseSize}px`;
      item.style.transform = 'translateY(0)';
    });
  });

  // App Launch Click Animation
  items.forEach(item => {
    item.addEventListener('click', () => {
      const targetWindowId = item.getAttribute('data-window-target');
      if (targetWindowId) {
        const win = document.getElementById(targetWindowId);
        if (win) {
          win.style.display = 'flex';
          win.classList.remove('minimized');
          bringWindowToFront(win);
        }
      }
      
      // Apple dock bounce animation
      item.animate([
        { transform: 'translateY(0)' },
        { transform: 'translateY(-22px)' },
        { transform: 'translateY(0)' },
        { transform: 'translateY(-10px)' },
        { transform: 'translateY(0)' }
      ], {
        duration: 380,
        easing: 'cubic-bezier(0.16, 1, 0.3, 1)'
      });
    });
  });

  // Dynamic calendar date sync
  const now = new Date();
  const days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
  const calDay = document.getElementById('dockCalDay');
  const calDate = document.getElementById('dockCalDate');
  if (calDay) calDay.textContent = days[now.getDay()];
  if (calDate) calDate.textContent = now.getDate();
}

/* ========================================================= */
/* 6. WINDOW CONTROLS & DRAG                                 */
/* ========================================================= */
function initWindowControls() {
  const windows = document.querySelectorAll('.apple-window');

  windows.forEach(win => {
    // Focus window on click
    win.addEventListener('mousedown', () => bringWindowToFront(win));

    // Traffic Lights
    const closeBtn = win.querySelector('.traffic-light.close');
    const minBtn = win.querySelector('.traffic-light.minimize');
    const expBtn = win.querySelector('.traffic-light.expand');

    if (closeBtn) {
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        win.style.display = 'none';
      });
    }

    if (minBtn) {
      minBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        win.classList.add('minimized');
        setTimeout(() => win.style.display = 'none', 200);
      });
    }

    if (expBtn) {
      expBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        win.classList.toggle('maximized');
        const container = win.closest('.record-window-container');
        if (container) container.classList.toggle('is-maximized');
        if (win.classList.contains('maximized')) {
          win.dataset.prevTop = win.style.top;
          win.dataset.prevLeft = win.style.left;
          win.dataset.prevWidth = win.style.width;
          win.dataset.prevHeight = win.style.height;
          if (!win.classList.contains('active-canvas')) {
            win.style.top = '36px';
            win.style.left = '12px';
            win.style.width = 'calc(100vw - 24px)';
            win.style.height = 'calc(100vh - 120px)';
          }
        } else {
          if (!win.classList.contains('active-canvas')) {
            win.style.top = win.dataset.prevTop || '80px';
            win.style.left = win.dataset.prevLeft || '100px';
            win.style.width = win.dataset.prevWidth || '860px';
            win.style.height = win.dataset.prevHeight || '540px';
          }
        }
      });
    }

    // Draggable Titlebar
    const titlebar = win.querySelector('.apple-titlebar');
    if (titlebar) {
      let isDragging = false;
      let startX, startY, startLeft, startTop;

      titlebar.addEventListener('mousedown', (e) => {
        if (e.target.closest('.apple-traffic-lights')) return;
        if (win.classList.contains('maximized')) return;
        if (win.classList.contains('active-canvas')) return;

        isDragging = true;
        startX = e.clientX;
        startY = e.clientY;
        const rect = win.getBoundingClientRect();
        startLeft = rect.left;
        startTop = rect.top;

        function onMouseMove(ev) {
          if (!isDragging) return;
          const deltaX = ev.clientX - startX;
          const deltaY = ev.clientY - startY;
          win.style.position = 'fixed';
          win.style.left = `${Math.max(0, startLeft + deltaX)}px`;
          win.style.top = `${Math.max(30, startTop + deltaY)}px`;
        }

        function onMouseUp() {
          isDragging = false;
          document.removeEventListener('mousemove', onMouseMove);
          document.removeEventListener('mouseup', onMouseUp);
        }

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
      });
    }
  });
}

let topZIndex = 100;
function bringWindowToFront(win) {
  topZIndex += 1;
  win.style.zIndex = topZIndex;
  document.querySelectorAll('.apple-window').forEach(w => w.classList.remove('active'));
  win.classList.add('active');
}

/* ========================================================= */
/* 7. DARK / LIGHT THEME TOGGLE                              */
/* ========================================================= */
function initThemeToggle() {
  const toggleBtn = document.getElementById('themeToggleBtn');
  if (!toggleBtn) return;

  toggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
  });
}
