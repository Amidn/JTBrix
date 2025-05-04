from flask import Flask
from JTBrix.ui.main import ui, submitted_results
from JTBrix.questionnaire.screens import screens
from JTBrix.experiment.run_session import run_unique_test
from JTBrix.questionnaire import screens as screen_module
from JTBrix.utils import find_free_port
import os
import webbrowser





if __name__ == "__main__":
    config = {
        "main_text": "Please read carefully before starting...",
        "checkbox_text": "I agree to participate.",
        "button_text": "Begin",
        "button_color": "#28a745",
        "video_filename": "FB.mp4",
        "question_data": [
            ("Pick a fruit:", "Apple", "Banana", "red", "yellow", "p.jpeg"),
            ("Pick a car:", "Tesla", "Ford", "blue", "gray", "p.jpeg"),
            ("Pick a city:", "Padova", "Bari", "navy", "olive", "p.jpeg")
        ],
        "final_options": ["Happy", "Neutral", "Sad"],
        "final_colors": ["green", "gray", "red"],
        "final_question": "How do you feel?"
    }



    results = run_unique_test(config, static_folder="/Users/amid/GitHub/JTBrix/Example/static/")
    print(results)


