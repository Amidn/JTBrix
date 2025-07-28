export function loadPage(container, next) {
  container.innerHTML = `
    <style>
        html, body {
            height: 100%;
            margin: 0;
            background: rgba(83, 108, 199, 0.288);
            font-family: Arial, sans-serif;
        }

        #popup {
            width: 33vw;
            height: 33vh;
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            align-items: center;
            margin: auto;
            position: absolute;
            top: 0; bottom: 0; left: 0; right: 0;
        }

        #popup h2 {
            text-align: center;
            color: black;
        }

        #popup button {
            padding: 10px;
            margin: 5px;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 1em;
            cursor: pointer;
        }
    </style>

    <div id="popup">
        <h2>Wie sicher bist du dir?</h2>
        <div>
            
                <button style="background:gray;" data-answer="Nicht so sicher">Nicht so sicher</button>
            
                <button style="background:gray;" data-answer="Ziemlich sicher">Ziemlich sicher</button>
            
                <button style="background:gray;" data-answer="Ganz sicher">Ganz sicher</button>
            
        </div>
    </div>
  `;

  const startTime = Date.now();

  document.querySelectorAll('#popup button').forEach(btn => {
    btn.addEventListener('click', () => {
      const answer = btn.getAttribute('data-answer');
      const duration = Date.now() - startTime;

      const data = {
        popup_9: answer,
        popup_9_time: duration
      };

      jatos.appendResultData(data);
      window.jatosData = { ...(window.jatosData || {}), ...data };

      next();
    });
  });
}