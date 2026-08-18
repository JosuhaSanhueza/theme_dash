/**
 * ORIONSHIELD SAAS DASHBOARD THEME - APP CONTROLLER (app.js)
 * Controls sidebar toggle, dark/light theme switcher, dropdowns, and interactive UI states.
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initSidebar();
  initDropdowns();
});

/**
 * Initialize Dark / Light Theme with localStorage persistence
 */
function initTheme() {
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const savedTheme = localStorage.getItem('orion_theme') || 'light';
  
  // Set initial theme
  setTheme(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const currentTheme = document.documentElement.getAttribute('data-bs-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      setTheme(newTheme);
    });
  }
}

function setTheme(theme) {
  document.documentElement.setAttribute('data-bs-theme', theme);
  localStorage.setItem('orion_theme', theme);
  
  const icon = document.querySelector('#theme-toggle-btn i, #theme-toggle-btn .theme-icon');
  if (icon) {
    if (theme === 'dark') {
      icon.className = 'fa-solid fa-sun theme-icon';
    } else {
      icon.className = 'fa-solid fa-moon theme-icon';
    }
  }
}

/**
 * Initialize Sidebar Toggle (Expanded / Collapsed Mini-Sidebar)
 */
function initSidebar() {
  const sidebarToggleBtn = document.getElementById('sidebar-toggle');
  const savedSidebarState = localStorage.getItem('orion_sidebar') || 'expanded';

  if (savedSidebarState === 'collapsed') {
    document.body.classList.add('sidebar-collapsed');
    document.documentElement.classList.remove('sidebar-collapsed-init');
    updateToggleIcon(true);
  } else {
    document.body.classList.remove('sidebar-collapsed');
    document.documentElement.classList.remove('sidebar-collapsed-init');
    updateToggleIcon(false);
  }

  if (sidebarToggleBtn) {
    sidebarToggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      
      const isCollapsed = document.body.classList.toggle('sidebar-collapsed');
      localStorage.setItem('orion_sidebar', isCollapsed ? 'collapsed' : 'expanded');
      updateToggleIcon(isCollapsed);
    });
  }

  // Mobile Hamburger Toggle & Backdrop Overlay
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const sidebarOverlay = document.getElementById('sidebar-overlay');

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      document.body.classList.toggle('sidebar-mobile-open');
    });
  }

  if (sidebarOverlay) {
    sidebarOverlay.addEventListener('click', () => {
      document.body.classList.remove('sidebar-mobile-open');
    });
  }

  // Close mobile sidebar on menu link click
  const navLinks = document.querySelectorAll('.sidebar-menu .menu-link:not([data-toggle="submenu"])');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      document.body.classList.remove('sidebar-mobile-open');
    });
  });

  // Ver Más scroll handler & dynamic visibility for sidebar menu
  const btnSidebarMore = document.getElementById('btn-sidebar-more');
  const sidebarWrapper = document.getElementById('sidebar-menu-wrapper');
  
  function checkSidebarOverflow() {
    if (btnSidebarMore && sidebarWrapper) {
      // Check if scrollable content height exceeds wrapper visible height
      const hasOverflow = sidebarWrapper.scrollHeight - sidebarWrapper.scrollTop - sidebarWrapper.clientHeight > 15;
      if (hasOverflow && !document.body.classList.contains('sidebar-collapsed')) {
        btnSidebarMore.style.display = 'flex';
      } else {
        btnSidebarMore.style.display = 'none';
      }
    }
  }

  if (btnSidebarMore && sidebarWrapper) {
    btnSidebarMore.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      sidebarWrapper.scrollBy({ top: 120, behavior: 'smooth' });
    });

    sidebarWrapper.addEventListener('scroll', checkSidebarOverflow);
    window.addEventListener('resize', checkSidebarOverflow);
    setTimeout(checkSidebarOverflow, 300);
  }

  // Sidebar Submenu Collapsible Accordion
  const menuLinks = document.querySelectorAll('.menu-link[data-toggle="submenu"]');
  menuLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();

      // If sidebar is collapsed, expanding a submenu automatically expands the sidebar
      if (document.body.classList.contains('sidebar-collapsed')) {
        document.body.classList.remove('sidebar-collapsed');
        localStorage.setItem('orion_sidebar', 'expanded');
        updateToggleIcon(false);
      }

      const parentItem = link.closest('.menu-item');
      
      // Close other open submenus
      document.querySelectorAll('.menu-item.open').forEach(item => {
        if (item !== parentItem) {
          item.classList.remove('open');
        }
      });

      parentItem.classList.toggle('open');
    });
  });
}

function updateToggleIcon(isCollapsed) {
  const toggleIcon = document.querySelector('#sidebar-toggle .toggle-icon');
  if (toggleIcon) {
    if (isCollapsed) {
      toggleIcon.className = 'fa-solid fa-outdent toggle-icon';
    } else {
      toggleIcon.className = 'fa-solid fa-indent toggle-icon';
    }
  }
}

/**
 * Initialize Dropdown Menus (Notifications, Profile)
 */
function initDropdowns() {
  const dropdownButtons = document.querySelectorAll('[data-toggle="dropdown"]');

  dropdownButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      
      const targetId = btn.getAttribute('data-target');
      const dropdownMenu = targetId ? document.getElementById(targetId) : btn.nextElementSibling;
      
      // Close all other open dropdowns
      document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
        if (menu !== dropdownMenu) {
          menu.classList.remove('show');
        }
      });

      if (dropdownMenu) {
        dropdownMenu.classList.toggle('show');
      }
    });
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', () => {
    document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
      menu.classList.remove('show');
    });
  });
}
