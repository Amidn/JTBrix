from flask import Blueprint, render_template_string
import os
from flask import Blueprint, request, render_template


screens = Blueprint("screens", __name__)
from flask import render_template, abort
from JTBrix import screen_config

@screens.route("/screen/question/<int:index>")
def show_question(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "question":
        return abort(400, description="Expected a question step")

    prompt = step.get("prompt", "")
    options = step.get("options", [])
    colors = step.get("colors", [])
    image = step.get("image", "")

    if len(options) != 2 or len(colors) != 2:
        return abort(400, description="Questions must have 2 options and 2 colors")

    return render_template("question_screen.html",
        index=index,
        question=prompt,
        option1=options[0],
        option2=options[1],
        color1=colors[0],
        color2=colors[1],
        image=image
    )

@screens.route("/screen/video")
def show_video():
    filename = request.args.get("filename")
    if not filename:
        return "Missing video filename", 400

    return render_template("video_screen.html", filename=filename)


@screens.route("/screen/consent")
def screen_consent():
    consent_step = next((step for step in screen_config.flow_config if step.get("type") == "consent"), None)
    if not consent_step:
        return "<p>Consent step not found.</p>", 404

    main_text = consent_step.get("main_text", "Please read the following.")
    checkbox_text = consent_step.get("checkbox_text", "I agree to participate.")
    button_text = consent_step.get("button_text", "Begin")
    button_color = consent_step.get("button_color", "#007BFF")

    html = f"""
    <div style="padding: 40px; color: black; background: white; height: 100%;">
        <p style="font-size: 18px;">{main_text}</p>
        <label>
            <input type="checkbox" id="agreeBox"> {checkbox_text}
        </label><br><br>
        <button id="startBtn" disabled style="padding: 10px 20px; font-size: 16px; background: {button_color}; color: white; border: none; border-radius: 6px;">{button_text}</button>
    </div>
    <script>
        function toggleButton() {{
            const btn = document.getElementById('startBtn');
            const box = document.getElementById('agreeBox');
            btn.disabled = !box.checked;
        }}

        document.addEventListener("DOMContentLoaded", function () {{
            document.getElementById("agreeBox").addEventListener("change", toggleButton);
            document.getElementById("startBtn").addEventListener("click", function () {{
                window.parent.nextStep();
            }});
        }});
    </script>
    """
    return render_template_string(html)



@screens.route("/screen/popup/<int:index>")
def screen_popup(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "popup":
        return abort(400, description="Expected a popup step")

    question = step.get("question", "")
    options = step.get("options", [])
    colors = step.get("colors", [])

    if len(options) != 3 or len(colors) != 3:
        return abort(400, description="Popup must have 3 options and 3 colors")

    html = f"""
    <div style="height:100%; display: flex; align-items: center; justify-content: center;">
        <div id="popup" style="width: 33vw; height: 33vh; background: white; border-radius: 12px; padding: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.3); display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
            <h2>{question}</h2>
            <div>
                <button style="background:{colors[0]}; padding:10px; margin:5px; color:white;" onclick="submitPopup('{options[0]}')">{options[0]}</button>
                <button style="background:{colors[1]}; padding:10px; margin:5px; color:white;" onclick="submitPopup('{options[1]}')">{options[1]}</button>
                <button style="background:{colors[2]}; padding:10px; margin:5px; color:white;" onclick="submitPopup('{options[2]}')">{options[2]}</button>
            </div>
        </div>
    </div>
    <script>
        const startTime = Date.now();
        function submitPopup(answer) {{
            const time = (Date.now() - startTime) / 1000;
            window.parent.submitPopup(answer, time);
        }}
    </script>
    """
    return render_template_string(html)