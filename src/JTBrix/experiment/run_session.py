from flask import Flask, request, render_template_string
import threading
import time
import webbrowser

from JTBrix.stimuli import register_video
from JTBrix.questionnaire.Survey import questioner
import os


def sequence(app, port, *question_data_list):
    result = {'answers': [], 'times': [], 'expected': len(question_data_list)}
    done_flag = {'done': False}

    @app.route('/favicon.ico')
    def favicon():
        return '', 204
    
    register_video(app, video_path="static/FB.mp4")#, done_flag=done_flag)

    for i, question_data in enumerate(question_data_list, start=1):
        question, option1, option2, color1, color2, image_path = question_data
        questioner(app, question, option1, option2, color1, color2, image_path, result, index=str(i))

    def start_flask():
        app.run(port=port, debug=False)

    threading.Thread(target=start_flask, daemon=True).start()
    webbrowser.open(f"http://127.0.0.1:{port}/consent")
  #  webbrowser.open(f"http://127.0.0.1:{port}/video")

    while len(result['answers']) < result['expected']:
        time.sleep(0.1)

    return result['answers'], result['times']


from flask import Flask
from JTBrix.ui.main import ui, submitted_results
from JTBrix.questionnaire.screens import screens
from JTBrix.questionnaire import screens as screen_module
from JTBrix.utils import find_free_port
import os
import webbrowser


def run_unique_test(config: dict, static_folder: str):
    # Apply dynamic config to screen module
    screen_module.MAIN_TEXT = config.get("main_text", "")
    screen_module.CHECKBOX_TEXT = config.get("checkbox_text", "")
    screen_module.BUTTON_TEXT = config.get("button_text", "")
    screen_module.BUTTON_COLOR = config.get("button_color", "#007BFF")
    screen_module.VIDEO_FILENAME = config.get("video_filename", "")
    screen_module.QUESTION_DATA = config.get("question_data", [])
    screen_module.FINAL_OPTIONS = config.get("final_options", [])
    screen_module.FINAL_COLORS = config.get("final_colors", [])
    screen_module.FINAL_QUESTION = config.get("final_question", "")

    # Setup Flask app
    app = Flask(__name__, static_folder=os.path.abspath(static_folder))
    app.register_blueprint(ui)
    app.register_blueprint(screens)

    port = find_free_port()
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        webbrowser.open(f"http://127.0.0.1:{port}/experiment")

    app.run(port=port, debug=True)

    return submitted_results
