from flask import Flask
from JTBrix.ui.main import ui
import os 
from JTBrix.questionnaire.screens import screens
from JTBrix.ui.main import submitted_results

# Override screen_module variables before registering blueprint
from JTBrix.questionnaire import screens as screen_module



screen_module.MAIN_TEXT = "Before continuing, please read the following instructions carefully..."
screen_module.CHECKBOX_TEXT = "I have read and agree to the conditions."
screen_module.BUTTON_TEXT = "Start"
screen_module.BUTTON_COLOR = "#007BFF"
screen_module.VIDEO_FILENAME = "FB.mp4"
screen_module.QUESTION_DATA = [
    ("Which fruit do you prefer?", "Apple", "Banana", "red", "goldenrod", "p.jpeg"),
    ("Which car do you prefer?", "Tesla", "Ford", "blue", "gray", "p.jpeg"),
    ("Which city do you prefer?", "Padova", "Bari", "blue", "gray", "p.jpeg")
]
screen_module.FINAL_OPTIONS = ["Happy", "Neutral", "Sad"]
screen_module.FINAL_COLORS = ["green", "gray", "red"]
screen_module.FINAL_QUESTION = "Final question: How did you feel?"

 

app = Flask(__name__, static_folder="static")
app.register_blueprint(ui)
app.register_blueprint(screens)

if __name__ == "__main__":
    from JTBrix.utils import find_free_port
    import webbrowser
    import os

    port = find_free_port()
    # Open browser only once, even with Flask reloader
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        webbrowser.open(f"http://127.0.0.1:{port}/experiment")
    app.run(port=port, debug=True)
    result=  submitted_results
    print (result)