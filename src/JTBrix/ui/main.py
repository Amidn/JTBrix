from flask import Blueprint, request, render_template_string
import json

ui = Blueprint("ui", __name__)

# Store submitted results in memory (you can later export or print)
submitted_results = []

@ui.route("/experiment")
def experiment():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Experiment</title>
        <meta charset="UTF-8">
        <style>
            html, body {
                margin: 0;
                padding: 0;
                height: 100%;
                font-family: Arial, sans-serif;
                background-color: black;
            }
            #content {
                width: 100%;
                height: 100%;
                overflow: hidden;
            }
            iframe {
                border: none;
            }
        </style>
    </head>
    <body>
        <div id="content"></div>

        <script>
            let currentQuestion = -1;
            const totalQuestions = 3;
            const results = { answers: [], times: [] };
            const popupResult = {};

            function loadScreen(endpoint) {
                const contentDiv = document.getElementById('content');
                contentDiv.innerHTML = ''; // Clear previous
                const iframe = document.createElement('iframe');
                iframe.style.width = '100%';
                iframe.style.height = '100%';
                iframe.src = endpoint;
                contentDiv.appendChild(iframe);
            }

            function start() {
                document.documentElement.requestFullscreen().catch(e => {});
                loadScreen('/screen/consent');
            }

            function proceedToVideo() {
                loadScreen('/screen/video');
            }

            function proceedToNextQuestion(answer, time) {
                if (currentQuestion >= 0) {
                    results.answers.push(answer);
                    results.times.push(time);
                }
                currentQuestion++;
                if (currentQuestion < totalQuestions) {
                    loadScreen(`/screen/question/${currentQuestion + 1}`);
                } else {
                    loadScreen('/screen/popup');
                }
            }

            function submitPopup(answer, time) {
                popupResult.answer = answer;
                popupResult.time = time;

                const fullResults = {
                    answers: results.answers,
                    times: results.times,
                    final_answer: popupResult.answer,
                    final_time: popupResult.time
                };

                fetch("/submit_results", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(fullResults)
                }).then(() => {
                    document.getElementById('content').innerHTML = '<h1>Thank you!</h1>';
                    console.log("Results submitted:", fullResults);
                });
            }

            start();
        </script>
    </body>
    </html>
    """

@ui.route("/submit_results", methods=["POST"])
def submit_results():
    data = request.get_json()
    print("✅ Received Results:", json.dumps(data, indent=2))

    # Store in memory
    submitted_results.append(data)

    # Optionally save to file
    # with open("results.jsonl", "a") as f:
    #     f.write(json.dumps(data) + "\n")

    return "", 204

@ui.route("/view_results")
def view_results():
    return "<pre>" + json.dumps(submitted_results, indent=2) + "</pre>"