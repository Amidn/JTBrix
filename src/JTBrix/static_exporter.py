import os
import random
import shutil
import yaml
from jinja2 import Template

from JTBrix.utils.config import read_experiment_config

class StaticExporter:
    def __init__(self, static_folder="static", config_path="data/config.yml", template_dir="templates", output_path="data/results"):
        self.config_path = config_path
        self.template_dir = template_dir
        self.output_path = output_path
        self.static_folder = static_folder
        self.blocks = []
        self.ordered_blocks = []

    def load_config(self):
        config, order = read_experiment_config(self.config_path)
        self.blocks = config
        self.ordered_blocks = order



if __name__ == "__main__":
    exporter = StaticExporter()
    exporter.load_config()

    print("✔️ Config successfully loaded.")
    print("\n🔹 All blocks from config (self.blocks):")
    for i, block in enumerate(exporter.blocks):
        print(f"  {i+1}. {block}")

    print("\n🔹 Ordered block references (self.ordered_blocks):")
    for i, block in enumerate(exporter.ordered_blocks):
        print(f"  {i+1}. {block}")

    print("\n🔹 Type of first item in ordered_blocks:", type(exporter.ordered_blocks[0]))