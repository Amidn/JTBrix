from JTBrix.ui.main import ui, submitted_results
from flask import Flask
import os
import webbrowser
from pathlib import Path
import JTBrix
from JTBrix.questionnaire.screens import screens
from JTBrix.utils import find_free_port
from JTBrix import screen_config
from JTBrix.utils.results import get_combined_results
import time

jtbrix_root = Path(JTBrix.__file__).parent
template_path = jtbrix_root / "templates"  # Now points to JTBrix/templates

import threading

def run_entire_test_config(config: dict, static_folder: str):
    screen_config.flow_config = config

    app = Flask(__name__, static_folder=os.path.abspath(static_folder), template_folder=template_path)
    app.register_blueprint(ui)
    app.register_blueprint(screens)

    port = find_free_port()

    def run_app():
        app.run(port=port, debug=False, use_reloader=False)

    thread = threading.Thread(target=run_app)
    thread.start()
    print (f"Flask app running on port {port}")
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        webbrowser.open(f"http://127.0.0.1:{port}/experiment")

    
    # Wait until any submission is marked as finished
    print("Waiting for experiment to finish...")
    start_time = time.time()
    timeout = 30  # seconds (10 minutes)
    while time.time() - start_time < timeout:
        if any(entry.get("finished") for entry in submitted_results):
            break
        time.sleep(1)  # Check every second
    #thread.join()  # Or implement your own wait logic

    return get_combined_results(submitted_results)