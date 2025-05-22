import os
import random
import shutil
import yaml
from jinja2 import Template

from JTBrix.utils.config import read_experiment_config

class StaticExporter:
    def __init__(self, static_folder="static", config_path="data/config.yml", template_dir="JS_Templates", output_path="data/results", repository_path="data/repository"):
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


    def render_consent_block(self, block, block_id,next_page): 
        """
        Renders the consent block using the consent_screen.html template.
        """
        consent_template = os.path.join(self.template_dir, "consent.html")
        if not os.path.isfile(consent_template):
            raise FileNotFoundError(f"Template not found: {consent_template}")

        with open(consent_template, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            next_step=next_page,
            main_text=block["main_text"],
            checkbox_texts=block["checkbox_text"],
            button_text=block["button_text"],
            button_color=block.get("button_color", "#007bff")  # default if missing
        )

        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_text_input_block(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
        template_path = os.path.join(self.template_dir, "text.html")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            id= block["id"],
            prompt= block["prompt"],
            placeholder= block["placeholder"],
            button_text= block["button_text"],
            next_step= next_page
            )
        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_dob_block(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
        template_path = os.path.join(self.template_dir, "dob.html")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            prompt= block["prompt"],
            next_step= next_page
            )
        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_dropdown_block(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
        template_path = os.path.join(self.template_dir, "dropdown.html")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            prompt= block["prompt"],
            options= block["options"],
            next_step= next_page
            )
        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered



    def render_video_block(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
        template_path = os.path.join(self.template_dir, "video.html")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            filename = block["video_filename"],
            id = block_id,
            next_step= next_page
            )
        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_question_block(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
        template_path = os.path.join(self.template_dir, "question.html")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            id=block_id,
            index=block_id,  # optional, used in <title>
            question=block["prompt"],
            option1=block["options"][0],
            option2=block["options"][1],
            color1=block["colors"][0],
            color2=block["colors"][1],
            image=block["image"],
            next_step=next_page
        )
        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_popup_block(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
       # template_path = os.path.join(self.template_dir, "popup.html")
        template_path = os.path.abspath(os.path.join(self.template_dir, "popup.html"))
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            id=block_id,
           # index=block_id,  # optional
            question=block["question"],
            options_colors=zip(block["options"], block["colors"]),
            next_step=next_page
        )

        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered



    def end(self, block, block_id, next_page):
        """
        Renders a text_input block using the text.html template.
        """
       # template_path = os.path.join(self.template_dir, "popup.html")
        template_path = os.path.abspath(os.path.join(self.template_dir, "end.html"))
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())


        rendered = template.render(
            message=block["message"],
            background=block["background"],
            text_color=block["text_color"]
        )

        # Save to HTML file
        output_dir = self.repository_path

        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create filename from block ID
        filename = f"page_{block_id}.html"
        file_path = os.path.join(output_dir, filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered





if __name__ == "__main__":
    exporter = StaticExporter( )
    exporter.load_config()
    


    block = {'type': 'consent', 
             'main_text': ' Liebe Teilnehmenden, Vielen Dank für dein Interesse! In dieser Studie geht es um die Beurteilungen von wahren und falschen Aussagen. Die Studie dauert ungefähr 5 Minuten. Mit Ihrer Teilnahme erklären Sie sich einverstanden, dass Ihre Daten pseudonymisiert und anonym verarbeitet werden. Ihre Daten werden gemäß DSGVO vertraulich behandelt und geschützt. Sie können Ihre Zustimmung jederzeit ohne Angabe von Gründen widerrufen. Verantwortlich für diese Studie sind Prof. Dr. Hannes Rakoczy, Dr. Marina Proft und Saba Amirhaftehran (Universität Göttingen)..',
             'checkbox_text': ['Hiermit bestätige ich, dass ich mindestens 18 Jahre alt bin und mit der Teilnahme an dieser Studie einverstanden bin.', 'Hiermit stimme ich der Datenerhebung und -verarbeitung zu gemäß Artikel 6 DSGVO.'], 
             'button_text': 'Start', 'button_color': '#28a745'}

    consent = exporter.render_consent_block(block, 1, "2")
    print(consent)
  
  
    block =    {'type': 'text_input', 
                'id': 'participant_first_name', 
                'prompt': 'Geben Sie bitte einen Codenamen für sich ein:', 
                'placeholder': 'Your full name', 
                'button_text': 'Weiter'}
    text_input = exporter.render_text_input_block(block, 2, "3")


    block =  {'type': 'dob', 'prompt': 'Geburtsdatum'}
    dob = exporter.render_dob_block(block, 3, "4")

    block = {'type': 'dropdown', 
            'prompt': 'Ist Deutsch deine Muttersprache??', 
            'options': ['Ja', 'Nein']}
    dropdown = exporter.render_dropdown_block(block, 4, "5")

    block = {'type': 'video', 'video_filename': 'GI.mp4'}
    video = exporter.render_video_block(block, 5, "6")

    block = {'type': 'question', 
             'prompt': 'In welcher Box ist ein Würfel?', 
             'options': ['Gelb', 'Grun'], 
             'colors': ['yellow', 'green'], 
             'image': 'GI.png'}

    question = exporter.render_question_block(block, 6, "7")


    block = {'type': 'popup', 
             'question': 'Wie sicher bist du dir?', 
             'options': ['Nicht so sicher', 'Ziemlich sicher', 'Ganz sicher'], 
             'colors': ['gray', 'gray', 'gray']}

    popup = exporter.render_popup_block(block, 7, "8")


    block = {
    'type': 'end',
    'message': 'Vielen Dank für Ihre Teilnahme an diesem Experiment.',
    'background': '#eeeeee',
    'text_color': '#333333'
}
    end = exporter.end(block, 8, "9")

    print("✔️ Config successfully loaded.")
    print("\n🔹 All blocks from config (self.blocks):")
    for i, block in enumerate(exporter.blocks):
        print(f"  {i+1}. {block}")

    print("\n🔹 Ordered block references (self.ordered_blocks):")
    for i, block in enumerate(exporter.ordered_blocks):
        print(f"  {i+1}. {block}")

    print("\n🔹 Type of first item in ordered_blocks:", type(exporter.ordered_blocks[0]))