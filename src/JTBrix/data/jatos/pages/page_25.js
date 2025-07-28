export function loadPage(container, next) {
  container.innerHTML = `
    <style>
        html, body {
            height: 100%;
            margin: 0;
            font-family: Arial, sans-serif;
            background: #eeeeee;
            color: #333333;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .message-box {
            max-width: 70vw;
            padding: 40px;
            font-size: 2em;
            line-height: 1.6em;
        }
    </style>

    <div class="message-box">
        Vielen Dank für Ihre Teilnahme an diesem Experiment.
    </div>
  `;

  history.replaceState(null, "", window.location.href);
  window.addEventListener("popstate", function () {
    location.replace(window.location.href);
  });
}