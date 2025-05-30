(async function(){
  const canvas = await html2canvas(document.body);
  const dataURL = canvas.toDataURL();
  fetch("/log", {
    method: "POST",
    body: JSON.stringify({ screenshot: dataURL }),
    headers: { 'Content-Type': 'application/json' }
  });
})();