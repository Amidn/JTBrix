 
from JTBrix.utils import find_free_port
from JTBrix.experiment import sequence
import os 
from flask import Flask, request, render_template_string
import webbrowser

from JTBrix.questionnaire.Survey import  register_popup_question, register_consent_page
app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"))# Flask(__name__)
free_port = find_free_port()


# Register the popup
wait_for_popup_response = register_popup_question(
    app,
    question_text="Final question: How did you feel?",
    options=["Happy", "Neutral", "Sad"],
    colors=["green", "gray", "red"],
    port=free_port,
)


register_consent_page(
    app,
    route="/consent",
    next_route="/video",
    main_text="Before continuing, please read the following instructions carefully...",
    checkbox_text="I have read and agree to the conditions.",
    button_text="Start",
    button_color="#007BFF"  # Bootstrap blue
)

Q1 = ("Which fruit do you prefer?", "Apple", "Banana", "red", "goldenrod", "static/p.jpeg")
Q2 = ("Which car do you prefer?", "Tesla", "Ford", "blue", "gray", "static/p.jpeg")
Q3 = ("Which city do you prefer?", "Padova", "Bari", "blue", "gray", "static/p.jpeg")
#webbrowser.open(f"http://127.0.0.1:{free_port}/consent")
answers, times = sequence(app, free_port, Q1, Q2, Q3)
print("Answers:", answers)
print("Times:", times)
# Now we can call the popup


# App is already running, so now we call the popup
answer, response_time = wait_for_popup_response()
print("Popup Answer:", answer)
print("Popup Time:", response_time)



