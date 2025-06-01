(function () {
    const tabId = Math.random().toString(36).substring(2);
    const log = (msg) => {
        fetch("/log", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                type: "tab_event",
                data: {
                    message: msg,
                    tabId: tabId
                }
            })
        });
    };

    // Signal this tab has loaded
    localStorage.setItem("xssbabe_ping", JSON.stringify({ tabId, time: Date.now() }));

    // Listen for other tabs
    window.addEventListener("storage", (e) => {
        if (e.key === "xssbabe_ping") {
            const data = JSON.parse(e.newValue);
            if (data.tabId !== tabId) {
                log(`Another tab opened with ID ${data.tabId}`);
            }
        }
    });

    // Optional: Monitor focus changes
    window.addEventListener("focus", () => log("Tab focus"));
    window.addEventListener("blur", () => log("Tab blur"));
})();
