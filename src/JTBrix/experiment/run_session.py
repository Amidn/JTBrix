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
