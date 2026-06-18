const express = require('express');
const path = require('path');
const app = express();

// Koyeb injects PORT automatically — never hardcode it
const PORT = process.env.PORT || 3000;

// Trust Koyeb's proxy (needed for correct IP / HTTPS headers)
app.set('trust proxy', 1);

// Serve everything in /public as static files
app.use(express.static(path.join(__dirname, 'public')));

// Fallback: any unknown route → index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Koyeb requires binding to 0.0.0.0, not just localhost
app.listen(PORT, '0.0.0.0', () => {
  const fqdn = process.env.KOYEB_PUBLIC_DOMAIN || `localhost:${PORT}`;
  console.log(`DevTools Suite running → https://${fqdn}`);
});
