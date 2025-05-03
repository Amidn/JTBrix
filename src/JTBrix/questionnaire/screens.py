from flask import Blueprint, render_template_string
import os

screens = Blueprint("screens", __name__)


# -------- Consent Page --------
@screens.route("/screen/consent")
def screen_consent():
    html = f"""
    <div style="padding: 40px; color: black; background: white; height: 100%;">
        <p style="font-size: 18px;">{MAIN_TEXT}</p>
        <label>
            <input type="checkbox" id="agreeBox"> {CHECKBOX_TEXT}
        </label><br><br>
        <button id="startBtn" disabled style="padding: 10px 20px; font-size: 16px; background: {BUTTON_COLOR}; color: white; border: none; border-radius: 6px;">{BUTTON_TEXT}</button>
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
                window.parent.proceedToVideo();
            }});
        }});
    </script>
    """
    return render_template_string(html)

# -------- Video Page --------
@screens.route("/screen/video")
def screen_video():
    video_path = f"/static/{VIDEO_FILENAME}"
    html = f"""
    <video id="videoPlayer" autoplay controls style="width: 100%; height: 100%; object-fit: contain;" onended="window.parent.proceedToNextQuestion('', 0)">
        <source src="{video_path}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """
    return render_template_string(html)

# -------- Question Pages --------
@screens.route("/screen/question/<int:index>")
def screen_question(index):
    try:
        question, opt1, opt2, color1, color2, image_file = QUESTION_DATA[index - 1]
    except IndexError:
        return "<p>Invalid question index</p>"

    image_url = f"/static/{image_file}"
    html = f"""
    <div style="text-align: center; padding: 40px; background: white; height: 100%;">
        <h2>{question}</h2>
        <div style="margin: 20px;">
            <button style="background:{color1}; color:white; padding:15px; margin:10px; border:none; border-radius:10px;" onclick="submitAnswer('{opt1}')">{opt1}</button>
            <button style="background:{color2}; color:white; padding:15px; margin:10px; border:none; border-radius:10px;" onclick="submitAnswer('{opt2}')">{opt2}</button>
        </div>
        <img src="{image_url}" alt="Image" style="max-height: 300px; max-width: 80%;">
    </div>
    <script>
        const startTime = Date.now();
        function submitAnswer(answer) {{
            const time = (Date.now() - startTime) / 1000;
            window.parent.proceedToNextQuestion(answer, time);
        }}
    </script>
    """
    return render_template_string(html)

# -------- Final Popup --------
@screens.route("/screen/popup")
def screen_popup():
    html = f"""
    <div style="height:100%; display: flex; align-items: center; justify-content: center;">
        <div id="popup" style="width: 33vw; height: 33vh; background: white; border-radius: 12px; padding: 20px; box-shadow: 0 0 20px rgba(0,0,0,0.3); display: flex; flex-direction: column; justify-content: space-around; align-items: center;">
            <h2>{FINAL_QUESTION}</h2>
            <div>
                <button style="background:{FINAL_COLORS[0]}; padding:10px; margin:5px; color:white;" onclick="submitPopup('{FINAL_OPTIONS[0]}')">{FINAL_OPTIONS[0]}</button>
                <button style="background:{FINAL_COLORS[1]}; padding:10px; margin:5px; color:white;" onclick="submitPopup('{FINAL_OPTIONS[1]}')">{FINAL_OPTIONS[1]}</button>
                <button style="background:{FINAL_COLORS[2]}; padding:10px; margin:5px; color:white;" onclick="submitPopup('{FINAL_OPTIONS[2]}')">{FINAL_OPTIONS[2]}</button>
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

