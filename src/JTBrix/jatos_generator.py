
import os
import random
import shutil
import yaml
from jinja2 import Template
from JTBrix.utils.config import read_experiment_config



class StaticExporter:
    def __init__(self, static_folder="static", config_path="data/config.yml", template_dir="JATOS_Templates", output_path="data/jatos", repository_path="data/jatos"):
        self.config_path = config_path
        self.template_dir = template_dir
        self.output_path = output_path
        self.static_folder = static_folder
        self.repository_path = repository_path
        self.blocks = []
        self.ordered_blocks = []

    def load_config(self):
        config, order = read_experiment_config(self.config_path, randomize=False)
        self.blocks = config
        self.ordered_blocks = order


    def get_block_type(self, block):
        """
        Returns the type of the given block.
        """
        return block.get("type", None)


    def render_consent_block(self, block, block_id, next_page): 
        """
        Renders the consent block using the consent.js.j2 template.
        """
        consent_template = os.path.join(self.template_dir, "consent.js.j2")
        if not os.path.isfile(consent_template):
            raise FileNotFoundError(f"Template not found: {consent_template}")

        with open(consent_template, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            next_step=next_page,
            main_text=block["main_text"],
            checkbox_texts=block["checkbox_text"],
            button_text=block["button_text"],
            button_color=block.get("button_color", "#007bff")
        )

        output_dir = self.repository_path
        os.makedirs(output_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(output_dir, "pages", filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_text_input_block(self, block, block_id, next_page): 
        """
        Renders a text_input block using the text.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "text.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            id=block["id"],
            prompt=block["prompt"],
            placeholder=block["placeholder"],
            button_text=block["button_text"],
            next_step=next_page
        )

        # Save as JS file inside /pages
        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered

    def render_dob_block(self, block, block_id, next_page):
        """
        Renders a date-of-birth block using the dob.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "dob.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            prompt=block["prompt"],
            next_step=next_page
        )

        # Save as JS file inside /pages
        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered

    def render_dropdown_block(self, block, block_id, next_page):
        """
        Renders a dropdown block using the dropdown.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "dropdown.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            prompt=block["prompt"],
            options=block["options"],
            next_step=next_page
        )

        # Save as JS file inside /pages
        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered

    def render_video_block(self, block, block_id, next_page):
        """
        Renders a video block using the video.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "video.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            filename=block["video_filename"],
            id=f"video_{block_id}",  # ensure unique identifier
            next_step=next_page
        )

        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered

    def render_question_block(self, block, block_id, next_page):
        """
        Renders a question block using the question.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "question.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            id=f"question_{block_id}",
            question=block["prompt"],
            option1=block["options"][0],
            option2=block["options"][1],
            color1=block["colors"][0],
            color2=block["colors"][1],
            image=block["image"],
            next_step=next_page
        )

        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered


    def render_popup_block(self, block, block_id, next_page):
        """
        Renders a popup block using the popup.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "popup.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            id=f"popup_{block_id}",
            question=block["question"],
            options_colors=zip(block["options"], block["colors"]),
            next_step=next_page
        )

        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered
    def end(self, block, block_id, next_page):
        """
        Renders the end screen using the end.js.j2 template.
        """
        template_path = os.path.join(self.template_dir, "end.js.j2")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())

        rendered = template.render(
            message=block["message"],
            background=block["background"],
            text_color=block["text_color"]
        )

        pages_dir = os.path.join(self.repository_path, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        filename = f"page_{block_id}.js"
        file_path = os.path.join(pages_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return rendered

    def render_all(self):
        """
        Renders all blocks in self.blocks sequentially by calling the appropriate render method
        based on each block's 'type'. Each rendered block is saved as an HTML file.
        """
        if not self.blocks:
            raise ValueError("No blocks loaded. Call load_config() first.")

        for idx, block in enumerate(self.blocks):
            block_type = block.get("type")
            block_id = idx + 1
            is_last_block = idx == len(self.blocks) - 1
            next_page = f"{block_id + 1}" if not is_last_block else None

            print(f"🔧 Rendering block {block_id}: type='{block_type}'")

            if block_type == "consent":
                self.render_consent_block(block, block_id, next_page)
            elif block_type == "text_input":
                self.render_text_input_block(block, block_id, next_page)
            elif block_type == "dob":
                self.render_dob_block(block, block_id, next_page)
            elif block_type == "dropdown":
                self.render_dropdown_block(block, block_id, next_page)
            elif block_type == "video":
                self.render_video_block(block, block_id, next_page)
            elif block_type == "question":
                self.render_question_block(block, block_id, next_page)
            elif block_type == "popup":
                self.render_popup_block(block, block_id, next_page)
            elif block_type == "end":
                self.end(block, block_id, next_page)
            else:
                raise ValueError(f"Unknown block type: {block_type}")

        print("All blocks rendered successfully.")

    def render_main(self):
        """
        Generates a central main.html to manage and load all other rendered pages via iframe and JavaScript.
        Categorizes blocks into pre_task, main_blocks, and post_task.
        Groups main_blocks into sublists starting with a video followed by 3 questions and 1 popup.
        Outputs these as distinct JS arrays, randomizes main_blocks order, and flattens for sequential loading.
        """
        # Categorize blocks by type
        pre_task = []
        main_blocks = []
        post_task = []

        # Collect blocks with their page filenames
        pages = [f"page_{i + 1}.js" for i in range(len(self.blocks))]

        # Build list of tuples: (block_type, page_filename)
        block_pages = [(block.get("type"), pages[i]) for i, block in enumerate(self.blocks)]

        # Separate pre_task, main_blocks, post_task based on block types
        # Assuming pre_task types: consent, text_input, dob, dropdown (or others before video)
        # main_blocks start from first video block to last popup before end
        # post_task types: end or others after main blocks

        # Find indices for main blocks start and end
        first_video_idx = None
        last_popup_idx = None
        for i, (btype, _) in enumerate(block_pages):
            if btype == "video" and first_video_idx is None:
                first_video_idx = i
            if btype == "popup":
                last_popup_idx = i

        if first_video_idx is None:
            first_video_idx = 0
        if last_popup_idx is None:
            last_popup_idx = len(block_pages) - 1

        # Assign blocks to pre_task, main_blocks, post_task
        pre_task = block_pages[:first_video_idx]
        main_blocks_raw = block_pages[first_video_idx:last_popup_idx+1]
        post_task = block_pages[last_popup_idx+1:]

        # Group main_blocks into chunks: video + 3 questions + 1 popup
        grouped_main_blocks = []
        i = 0
        while i < len(main_blocks_raw):
            group = []
            # video
            if i < len(main_blocks_raw) and main_blocks_raw[i][0] == "video":
                group.append(main_blocks_raw[i][1])
                i += 1
            else:
                # If no video at expected position, break to avoid infinite loop
                break
            # 3 questions
            for _ in range(3):
                if i < len(main_blocks_raw) and main_blocks_raw[i][0] == "question":
                    group.append(main_blocks_raw[i][1])
                    i += 1
                else:
                    break
            # 1 popup
            if i < len(main_blocks_raw) and main_blocks_raw[i][0] == "popup":
                group.append(main_blocks_raw[i][1])
                i += 1
            grouped_main_blocks.append(group)

        # JavaScript arrays for pages
        template_path = os.path.join(self.template_dir, "index_template.html")
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Missing template: {template_path}")

        with open(template_path, "r", encoding="utf-8") as f:
            template = Template(f.read())
        

        rendered = template.render(
            pre_task=[page for _, page in pre_task],
            main_blocks=grouped_main_blocks,
            post_task=[page for _, page in post_task]
        )

        file_path = os.path.join(self.repository_path, "main.html")
        os.makedirs(self.repository_path, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        print(" main.html generated successfully.")





if __name__ == "__main__":
    exporter = StaticExporter()
    exporter.load_config()
    print(" Config successfully loaded.")
    exporter.render_all()
    exporter.render_main()


    print(" Config successfully loaded.")
    print("\n All blocks from config (self.blocks):")
    for i, block in enumerate(exporter.blocks):
        print(f"  {i+1}. {block}")

    print("\n Ordered block references (self.ordered_blocks):")
    for i, block in enumerate(exporter.ordered_blocks):
        print(f"  {i+1}. {block}")

    print("\n Type of first item in ordered_blocks:", type(exporter.ordered_blocks[0]))