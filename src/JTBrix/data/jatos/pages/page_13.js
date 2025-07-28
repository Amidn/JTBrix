export function loadPage(container, next) {
  container.innerHTML = `
    <style>
        html, body {
            height: 100%;
            margin: 0;
            background: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }

        .wrapper {
            height: 100%;
            display: grid;
            grid-template-rows: 1fr 1fr 1fr;
            padding: 2em;
            box-sizing: border-box;
        }

        .cell {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        h1 { margin: 0; }

        .options {
            flex-direction: row;
            gap: 1.2em;
            transform: translateY(-2.5cm);
        }

        .options button {
            font-size: 1.2em;
            padding: 1em 2em;
            border: none;
            cursor: pointer;
        }

        .bottom {
            transform: translateY(-2.5cm);
        }

        img {
            max-width: 80vw;
            max-height: 28vh;
        }
    </style>

    <div class="wrapper">
        <div class="cell">
            <h1>Weiß der Elefant, dass eine Erdbeere in der grünen Box ist?</h1>
        </div>

        <div class="cell options">
            <button style="background-color: blue;" id="btn1"> Ja </button>
            <button style="background-color: blue;" id="btn2">Nein</button>
        </div>

        <div class="cell bottom">
            <img src="static/images/TB.png" alt="Question Image">
        </div>
    </div>
  `;

  const start = Date.now();

  const handleClick = (answer) => {
    const duration = Date.now() - start;

    const data = {
      question_13: answer,
      question_13_time: duration
    };

    jatos.appendResultData(data);
    window.jatosData = { ...(window.jatosData || {}), ...data };

    next();
  };

  document.getElementById("btn1").addEventListener("click", () => handleClick(" Ja "));
  document.getElementById("btn2").addEventListener("click", () => handleClick("Nein"));
}