window.addEventListener("storage", (event) => {
  if (event.key === "xss_babe_chat") {
    fetch("/log?tabmsg=" + encodeURIComponent(event.newValue));
  }
});

localStorage.setItem("xss_babe_chat", "hello from another tab");