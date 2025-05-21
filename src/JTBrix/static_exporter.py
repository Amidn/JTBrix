import os
import random
import shutil
import yaml
from jinja2 import Template

from JTBrix.utils.config import read_experiment_config

class StaticExporter:
    def __init__(self, static_folder="static", config_path="data/config.yml", template_dir="templates", output_path="data/results", repository_path="data/repository"):
        self.config_path = config_path
        self.template_dir = template_dir
        self.output_path = output_path
        self.static_folder = static_folder
        self.repository_path = repository_path
        self.blocks = []
        self.ordered_blocks = []

    def load_config(self):
        config, order = read_experiment_config(self.config_path)
        self.blocks = config
        self.ordered_blocks = order


    def get_block_type(self, block):
        """
        Returns the type of the given block.
        """
        return block.get("type", None)


    def render_consent_block(self, block):
        """
        Renders the consent block using the consent_screen.html template.
        """
        consent_template = os.path.join(self.template_dir, "consent_screen.html")
        if not os.path.isfile(consent_template):
            raise FileNotFoundError(f"Template not found: {consent_template}")

        with open(consent_template, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            main_text=block["main_text"],
            checkbox_texts=block["checkbox_text"],
            button_text=block["button_text"],
            button_color=block.get("button_color", "#007bff")  # default if missing
        )
        return rendered
    




if __name__ == "__main__":
    exporter = StaticExporter()
    exporter.load_config()
    
    block = {'type': 'consent', 
             'main_text': ' Liebe Teilnehmenden, Vielen Dank für dein Interesse! In dieser Studie geht es um die Beurteilungen von wahren und falschen Aussagen. Die Studie dauert ungefähr 5 Minuten. Mit Ihrer Teilnahme erklären Sie sich einverstanden, dass Ihre Daten pseudonymisiert und anonym verarbeitet werden. Ihre Daten werden gemäß DSGVO vertraulich behandelt und geschützt. Sie können Ihre Zustimmung jederzeit ohne Angabe von Gründen widerrufen. Verantwortlich für diese Studie sind Prof. Dr. Hannes Rakoczy, Dr. Marina Proft und Saba Amirhaftehran (Universität Göttingen)..', 
             'checkbox_text': ['Hiermit bestätige ich, dass ich mindestens 18 Jahre alt bin und mit der Teilnahme an dieser Studie einverstanden bin.', 'Hiermit stimme ich der Datenerhebung und -verarbeitung zu gemäß Artikel 6 DSGVO.'], 
             'button_text': 'Start', 
             'button_color': '#28a745'
             }


    consent_html = exporter.render_consent_block(block)

    print(consent_html)  # <--- This prints the rendered HTML
    # exporter.load_config()

    # print("✔️ Config successfully loaded.")
    # print("\n🔹 All blocks from config (self.blocks):")
    # for i, block in enumerate(exporter.blocks):
    #     print(f"  {i+1}. {block}")

    # print("\n🔹 Ordered block references (self.ordered_blocks):")
    # for i, block in enumerate(exporter.ordered_blocks):
    #     print(f"  {i+1}. {block}")

    # print("\n🔹 Type of first item in ordered_blocks:", type(exporter.ordered_blocks[0]))