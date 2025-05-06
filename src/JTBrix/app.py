import os 
from flask import Flask
from JTBrix.ui.main import ui
from JTBrix.questionnaire.screens import screens
from pathlib import Path
import JTBrix
jtbrix_root = Path(JTBrix.__file__).parent
template_path = jtbrix_root / "templates"  # Now points to JTBrix/templates
static_path = jtbrix_root / "data" / "static"


app = Flask(__name__, static_folder=static_path, template_folder=template_path)
app.register_blueprint(ui)
app.register_blueprint(screens)
