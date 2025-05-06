import os
from flask import Flask, request, jsonify
from pathlib import Path

from JTBrix.ui.main import ui
from JTBrix.questionnaire.screens import screens
from JTBrix.experiment.run_experiment import run_test
from JTBrix.utils.results import build_full_structured_result
from JTBrix.io.saving import save_structured_output

import JTBrix

# Setup paths
jtbrix_root = Path(JTBrix.__file__).parent


template_path = "/content/JTBrix/src/JTBrix/templates/" 
config_path =  "/content/JTBrix/src/JTBrix/data/config.yml"



static_path =  "/content/JTBrix/src/JTBrix/data/static/"

results_path = "/content/JTBrix/src/JTBrix/data/results/"




# Create the app
app = Flask(__name__, static_folder=static_path, template_folder=template_path)
app.register_blueprint(ui)
app.register_blueprint(screens)

# ✅ Add /run_experiment route
@app.route("/run_experiment")
def run_experiment():
    results, order = run_test(config_path, static_path , timeout=300, port =5500)
    structured_output = build_full_structured_result(results, config_path, execution_order=order)
    save_structured_output(structured_output, save_path=results_path, name="Test_data")
    return jsonify({"status": "success", "order": order, "summary": structured_output})