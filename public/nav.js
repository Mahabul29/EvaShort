// Shared sidebar navigation
function renderNav(activePage) {
  const pages = [
    { href: 'index.html',      icon: '⊞', label: 'Dashboard' },
    { href: 'calculator.html', icon: '∑', label: 'Calculator' },
    { href: 'converter.html',  icon: '⇌', label: 'Converter' },
    { href: 'password.html',   icon: '◈', label: 'Password' },
    { href: 'markdown.html',   icon: '✦', label: 'Markdown' },
    { href: 'speedtest.html',  icon: '⚡', label: 'Speed Test' },
    { href: 'qrcode.html',     icon: '▦', label: 'QR Code' },
    { href: 'image-tool.html', icon: '◻', label: 'Image Tool' },
    { href: 'todo.html',       icon: '✓', label: 'To-Do' },
  ];

  const links = pages.map(p => `
    <a href="${p.href}" class="nav-link${activePage === p.href ? ' active' : ''}">
      <span class="nav-icon">${p.icon}</span>
      ${p.label}
    </a>
  `).join('');

  return `
    <nav class="sidebar">
      <div class="sidebar-brand">
        <div class="brand-icon">⚙</div>
        <div>
          <div class="brand-name">DevTools</div>
          <div class="brand-sub">Utility Suite</div>
        </div>
      </div>
      <div class="nav-section">Tools</div>
      ${links}
    </nav>
  `;
}

function showToast(msg, type = '') {
  const t = document.createElement('div');
  t.className = `toast ${type}`;
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 2800);
        }

