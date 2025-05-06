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
template_path = jtbrix_root / "templates"
static_path = jtbrix_root / "data" / "static"

# Create the app
app = Flask(__name__, static_folder=static_path, template_folder=template_path)
app.register_blueprint(ui)
app.register_blueprint(screens)

# Add /run_experiment route
# @app.route("/run_experiment")
# def run_experiment():
#     results, order = run_test("data/config.yml", "data/static/", timeout=300)
#     structured_output = build_full_structured_result(results, "data/config.yml", execution_order=order)
#     save_structured_output(structured_output, save_path="data/results/", name="Test_data")
#     return jsonify({"status": "success", "order": order, "summary": structured_output})


if __name__ == "__main__":
    results, order = run_test("data/config.yml", "data/static/", timeout=300)
    structured_output = build_full_structured_result(results, "data/config.yml", execution_order=order)
    save_structured_output(structured_output, save_path="data/results/", name="Test_data")
    