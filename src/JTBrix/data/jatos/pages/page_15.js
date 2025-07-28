export function loadPage(container, next) {
  container.innerHTML = `
    <style>
      html, body { margin:0; padding:0; background:#000; }
      video {
        width:100vw; height:100vh;
        object-fit: contain;
        -webkit-touch-callout:none;
        user-select:none;
      }
    </style>
    <video id="vid"
           autoplay
           muted
           playsinline
           disablepictureinpicture
           controlslist="nodownload noremoteplayback nofullscreen">
      <source src="static/videos/GI.mp4" type="video/mp4">
      <source src="static/videos/GI.webm" type="video/webm">
      Your browser does not support the video tag.
    </video>
  `;

  const start = Date.now();
  const video = document.getElementById("vid");
  let lastSafeTime = 0;

  video.muted = true;

  video.addEventListener("timeupdate", () => {
    lastSafeTime = video.currentTime;
  });

  video.addEventListener("seeking", () => {
    if (Math.abs(video.currentTime - lastSafeTime) > 0.25) {
      video.currentTime = lastSafeTime;
    }
  });

  video.addEventListener("pause", () => {
    if (!video.ended) video.play();
  });

  video.addEventListener("ended", () => {
    const duration = Date.now() - start;

    const data = {
      video_15_video_time: duration
    };

    jatos.appendResultData(data);
    window.jatosData = { ...(window.jatosData || {}), ...data };

    next();
  });

  window.addEventListener("keydown", e => {
    if (e.code === "Space") {
      e.preventDefault();
    }
  });
}