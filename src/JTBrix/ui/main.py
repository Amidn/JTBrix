from flask import Blueprint, request, render_template_string
import json

ui = Blueprint("ui", __name__)

# Store submitted results in memory (you can later export or print)
submitted_results = []

@ui.route("/experiment")
def experiment():
    from JTBrix.screen_config import flow_config  # this will store current config

    flow_json = json.dumps(flow_config)  # injected from runner

    return render_template_string("""
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
            const flow = {{ flow_json | safe }};
            let stepIndex = -1;
            const results = { answers: [], times: [] };
            const popupResult = {};

            function loadScreen(screenUrl) {
                const contentDiv = document.getElementById('content');
                contentDiv.innerHTML = '';
                const iframe = document.createElement('iframe');
                iframe.style.width = '100%';
                iframe.style.height = '100%';
                iframe.src = screenUrl;
                contentDiv.appendChild(iframe);
            }

            function nextStep(answer = null, time = null) {
                if (stepIndex >= 0 && flow[stepIndex].type === 'question') {
                    results.answers.push(answer);
                    results.times.push(time);
                }
                if (stepIndex >= 0 && flow[stepIndex].type === 'popup') {
                    popupResult.answer = answer;
                    popupResult.time = time;
                }

                stepIndex++;

                if (stepIndex >= flow.length) return;

                const step = flow[stepIndex];
                if (step.type === "consent") {
                    loadScreen("/screen/consent");
                } else if (step.type === "video") {
                    loadScreen(`/screen/video?filename=${encodeURIComponent(step.video_filename)}`);
                } else if (step.type === "question") {
                    loadScreen(`/screen/question/${stepIndex}`);
                } else if (step.type === "popup") {
                    loadScreen(`/screen/popup/${stepIndex}`);
                } else if (step.type === "end") {
                    const fullResults = {
                        answers: results.answers,
                        times: results.times,
                        final_answer: popupResult.answer,
                        final_time: popupResult.time
                    };
                    fetch("/submit_results", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify(fullResults)
                    }).then(() => {
                        const endHTML = `
                            <div style="display: flex; justify-content: center; align-items: center; height: 100vh;
                                        background: ${step.background || "#f0f0f0"}; color: ${step.text_color || "#333"}; font-family: Arial;">
                                <div style="text-align: center;">
                                    <h1>${step.message || "Thank you for your participation!"}</h1>
                                    <button onclick="document.exitFullscreen()" style="margin-top: 20px; padding: 10px 20px; font-size: 16px;">
                                        Exit Fullscreen
                                    </button>
                                </div>
                            </div>`;
                        document.getElementById('content').innerHTML = endHTML;
                    });
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
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(fullResults)
                }).then(() => {
                    document.getElementById('content').innerHTML = '<h1>Thank you!</h1>';
                    console.log("Results submitted:", fullResults);
                });
            }

            document.documentElement.requestFullscreen().catch(e => {});
            nextStep();
        </script>
    </body>
    </html>
    """, flow_json=flow_json)


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