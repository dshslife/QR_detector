
// Get the video element
const video = document.querySelector('#video')
// Check if device has camera
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  // Use video without audio
  const constraints = { 
    video: true,
    audio: false
  }
  
  // Start video stream
  navigator.mediaDevices.getUserMedia(constraints).then(stream => video.srcObject = stream);
}