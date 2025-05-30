(function(){
  const info = {
    ua: navigator.userAgent,
    lang: navigator.language,
    tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
    screen: `${screen.width}x${screen.height}`,
  };
  fetch("/log?fp=" + encodeURIComponent(JSON.stringify(info)));
})();