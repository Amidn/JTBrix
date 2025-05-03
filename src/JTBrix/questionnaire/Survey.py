from flask import request, render_template_string
import os
import threading
import time
import webbrowser


# {f'window.location.href="/question/{int(index) + 1}";' if int(index) < result["expected"] else 'document.body.innerHTML = "<h2>Thank you!</h2>";'}

def questioner(app, question, option1, option2, color1, color2, image_path, result, index):
    """
    Registers /question/<index> and /submit/<index> routes with unique endpoint names.
    """

    image_filename = os.path.basename(image_path)
    image_url = f"/static/{image_filename}"

    html_template = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <title>Question {index}</title>
        <style>
            body {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                height: 100vh;
                margin: 0;
            }}
            h2 {{
                margin-bottom: 30px;
                text-align: center;
            }}
            .option {{
                width: 300px;
                height: 60px;
                margin: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 18px;
                cursor: pointer;
                border-radius: 10px;
                color: white;
            }}
            img {{
                margin-top: 30px;
                max-width: 80%;
                max-height: 300px;
                object-fit: contain;
            }}
        </style>
    </head>
    <body>
        <h2>{question}</h2>
        <div class="option" style="background-color: {color1};" onclick="submitAnswer('{option1}')">{option1}</div>
        <div class="option" style="background-color: {color2};" onclick="submitAnswer('{option2}')">{option2}</div>
        <img src="{image_url}" alt="Image">
        
        <script>
            const startTime = Date.now();
            function submitAnswer(answer) {{
                const elapsed = (Date.now() - startTime) / 1000;
                fetch('/submit/{index}', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    body: JSON.stringify({{answer: answer, time: elapsed}})
                }}).then(() => {{
                    {f'window.location.href="/question/{int(index) + 1}";' if int(index) < result["expected"] else 'window.location.href="/popup";'}
                }});
            }}
        </script>
    </body>
    </html>
    """

    # Define question page handler
    def question_page():
        return render_template_string(html_template)
    
    app.add_url_rule(
        f'/question/{index}',
        endpoint=f'question_page_{index}',
        view_func=question_page
    )

    # Define submit handler
    def submit_answer():
        data = request.get_json()
        result['answers'].append(data['answer'])
        result['times'].append(data['time'])
        print(f"Submitted index: {index}, expected: {result['expected']}")
        # if int(index) < result['expected']:
        #     return f"<script>window.location.href='/question/{int(index) + 1}'</script>"
        # else:
        #     return "<h2>Thank you!</h2>"
        if int(index) < result['expected']:
            return f"<script>window.location.href='/question/{int(index) + 1}'</script>"
        else:
            return f"<script>window.location.href='/popup'</script>"

    app.add_url_rule(
        f'/submit/{index}',
        endpoint=f'submit_answer_{index}',
        view_func=submit_answer,
        methods=['POST']
    )


def register_popup_question(app, question_text, options, colors, port):
    assert len(options) == 3 and len(colors) == 3, "Must provide 3 options and 3 colors"
    result = {}


    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Popup Question</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                height: 100vh;
                background-color: rgba(0, 0, 0, 0.5);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: Arial, sans-serif;
            }}
            #popup {{
                width: 33vw;
                height: 33vh;
                background-color: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 0 20px rgba(0,0,0,0.3);
                display: flex;
                flex-direction: column;
                justify-content: space-around;
                align-items: center;
            }}
            h2 {{
                text-align: center;
                font-size: 20px;
            }}
            .answer {{
                width: 80%;
                padding: 10px;
                margin: 5px;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                text-align: center;
                font-size: 16px;
            }}
        </style>
    </head>
    <body>
        <div id="popup">
            <h2>{question_text}</h2>
            <div class="answer" style="background-color:{colors[0]};" onclick="submitAnswer('{options[0]}')">{options[0]}</div>
            <div class="answer" style="background-color:{colors[1]};" onclick="submitAnswer('{options[1]}')">{options[1]}</div>
            <div class="answer" style="background-color:{colors[2]};" onclick="submitAnswer('{options[2]}')">{options[2]}</div>
        </div>

        <script>
            const startTime = Date.now();
            function submitAnswer(answer) {{
                const elapsed = (Date.now() - startTime) / 1000;
                fetch('/popup_submit', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    body: JSON.stringify({{ answer: answer, time: elapsed }})
                }}).then(() => {{
                    document.body.innerHTML = "<h2>Thanks!</h2>";
                }});
            }}
        </script>
    </body>
    </html>
    """

    @app.route('/popup')
    def popup_page():
        return render_template_string(html_template)

    @app.route('/popup_submit', methods=['POST'])
    def popup_submit():
        data = request.get_json()
        result['answer'] = data['answer']
        result['time'] = data['time']
        return '', 204

    def wait_for_response():
       # webbrowser.open(f"http://127.0.0.1:{port}/popup")  # Assumes app is already running
        while 'answer' not in result:
            time.sleep(0.1)
        return result['answer'], result['time']

    return wait_for_response


def register_consent_page1(app, route, next_route, main_text, checkbox_text, button_text, button_color):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consent</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: 100vh;
            }}
            .content {{
                font-size: 18px;
                margin-bottom: 40px;
                white-space: pre-wrap;
            }}
            .checkbox {{
                display: flex;
                align-items: center;
                font-size: 16px;
                margin-bottom: 20px;
            }}
            #startBtn {{
                padding: 15px;
                font-size: 18px;
                border: none;
                border-radius: 8px;
                background-color: {button_color};
                color: white;
                cursor: not-allowed;
                opacity: 0.5;
                width: 200px;
                align-self: center;
            }}
            #startBtn.enabled {{
                cursor: pointer;
                opacity: 1.0;
            }}
        </style>
    </head>
    <body>
        <div class="content">{main_text}</div>
        <label class="checkbox">
            <input type="checkbox" id="agreeBox" onchange="toggleButton()"> {checkbox_text}
        </label>
        <button id="startBtn" onclick="proceed()" disabled>{button_text}</button>

        <script>
            function toggleButton() {{
                const btn = document.getElementById('startBtn');
                const box = document.getElementById('agreeBox');
                if (box.checked) {{
                    btn.classList.add("enabled");
                    btn.disabled = false;
                }} else {{
                    btn.classList.remove("enabled");
                    btn.disabled = true;
                }}
            }}
            function proceed() {{
                window.location.href = '{next_route}';
            }}
        </script>
    </body>
    </html>
    """

    app.add_url_rule(route, endpoint=f"consent_page_{route}", view_func=lambda: render_template_string(html_template))


def register_consent_page(app, route, next_route, main_text, checkbox_text, button_text, button_color):
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Consent</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                min-height: 100vh;
            }}
            .content {{
                font-size: 18px;
                margin-bottom: 40px;
                white-space: pre-wrap;
            }}
            .checkbox {{
                display: flex;
                align-items: center;
                font-size: 16px;
                margin-bottom: 20px;
            }}
            #startBtn {{
                padding: 15px;
                font-size: 18px;
                border: none;
                border-radius: 8px;
                background-color: {button_color};
                color: white;
                cursor: not-allowed;
                opacity: 0.5;
                width: 200px;
                align-self: center;
            }}
            #startBtn.enabled {{
                cursor: pointer;
                opacity: 1.0;
            }}
        </style>
    </head>
    <body>
        <div class="content">{main_text}</div>
        <label class="checkbox">
            <input type="checkbox" id="agreeBox" onchange="toggleButton()"> {checkbox_text}
        </label>
        <button id="startBtn" onclick="proceed()" disabled>{button_text}</button>

        <script>
            // Try to re-enter fullscreen if already allowed by browser
            document.addEventListener('DOMContentLoaded', () => {{
                if (document.fullscreenEnabled && !document.fullscreenElement) {{
                    document.documentElement.requestFullscreen().catch(e => console.log("Fullscreen not granted:", e));
                }}
            }});

            function toggleButton() {{
                const btn = document.getElementById('startBtn');
                const box = document.getElementById('agreeBox');
                if (box.checked) {{
                    btn.classList.add("enabled");
                    btn.disabled = false;
                }} else {{
                    btn.classList.remove("enabled");
                    btn.disabled = true;
                }}
            }}
            function proceed() {{
                window.location.href = '{next_route}';
            }}
        </script>
    </body>
    </html>
    """

    app.add_url_rule(route, endpoint=f"consent_page_{route}", view_func=lambda: render_template_string(html_template))

