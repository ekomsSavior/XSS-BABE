navigator.mediaDevices.getUserMedia({ video: true, audio: false })
  .then(stream => {
    fetch("/log?cam=access_granted");
    stream.getTracks().forEach(track => track.stop());
  })
  .catch(err => {
    fetch("/log?cam=denied");
  });