"""Top-level package for JTBrix."""

__author__ = """Amid Nayerhoda"""
__email__ = 'Nayerhoda@infn.it'
__version__ = '0.0.2'


# Import core functionality to the top level
from JTBrix.experiment import run_session  # Example: if you have a main entry point
from JTBrix.stimuli import play_video     # Example: expose frequently used tools
from JTBrix.questionnaire import Survey   # Example: expose a core class
from JTBrix.utils import port  # Example: utility functions
from JTBrix.ui import main  # Example: if you have a UI component


__all__ = [
    "run_session",
    "play_video",
    "Survey",
    "port",
    "main",
]