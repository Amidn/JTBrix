from flask import Flask
from JTBrix.experiment.run_session import run_entire_test_config
from JTBrix.screen_config import flow_config



config = [
    {
        "type": "consent",
        "main_text": "Please read carefully before starting... test1",
        "checkbox_text": "I agree to participate. test1",
        "button_text": "Begin1",
        "button_color": "#28a745"
    },
    {
        "type": "video",
        "video_filename": "FB.mp4"
    },
    {
        "type": "question",
        "prompt": "Pick a fruit:",
        "options": ["Apple", "Banana"],
        "colors": ["red", "yellow"],
        "image": "p.jpeg"
    },
    {
        "type": "question",
        "prompt": "Pick a car:",
        "options": ["Tesla", "Ford"],
        "colors": ["blue", "gray"],
        "image": "p.jpeg"
    },
    {
        "type": "question",
        "prompt": "Pick a city:",
        "options": ["Padova", "Bari"],
        "colors": ["navy", "olive"],
        "image": "p.jpeg"
    },
    {
        "type": "popup",
        "question": "How do you feel?",
        "options": ["Happy", "Neutral", "Sad"],
        "colors": ["green", "gray", "red"]
    },
    {
        "type": "end",
        "message": "You’ve completed the experiment. Please call the researcher.",
        "background": "#eeeeee",
        "text_color": "#333333"}
    ]
if __name__ == "__main__":


    flow_config.clear()
    flow_config.extend(config)
    results = run_entire_test_config(config, static_folder="/Users/amid/GitHub/JTBrix/Example/static/")
    print(results)

