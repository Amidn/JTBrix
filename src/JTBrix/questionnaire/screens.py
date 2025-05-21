from flask import Blueprint, render_template_string , request, render_template, abort
import os


screens = Blueprint("screens", __name__)



from JTBrix import screen_config

@screens.route("/screen/question/<int:index>")
def show_question(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "question":
        return abort(400, description="Expected a question step")

    prompt = step.get("prompt", "")
    options = step.get("options", [])
    colors = step.get("colors", [])
    image = step.get("image", "")

    if len(options) != 2 or len(colors) != 2:
        return abort(400, description="Questions must have 2 options and 2 colors")

    return render_template("question_screen.html",
        index=index,
        question=prompt,
        option1=options[0],
        option2=options[1],
        color1=colors[0],
        color2=colors[1],
        image=image
    )

@screens.route("/screen/video")
def show_video():
    filename = request.args.get("filename")
    if not filename:
        return "Missing video filename", 400

    return render_template("video_screen.html", filename=filename)


@screens.route("/screen/dob/<int:index>")
def screen_dob(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "dob":
        return abort(400, description="Expected a dob step")

    prompt = step.get("prompt", "Please enter your date of birth")

    return render_template("dob_screen.html", prompt=prompt)

@screens.route("/screen/consent")
def screen_consent():
    config = screen_config.flow_config[0]  # assuming consent is at index 0
    main_text = config.get("main_text", "Please read the following.")
    checkbox_texts = config.get("checkbox_text", ["I agree to participate."])
    button_text = config.get("button_text", "Begin")
    button_color = config.get("button_color", "#007BFF")

    return render_template(
        "consent_screen.html",
        main_text=main_text,
        checkbox_texts=checkbox_texts,
        button_text=button_text,
        button_color=button_color
    )

@screens.route("/screen/popup/<int:index>")
def screen_popup(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "popup":
        return abort(400, description="Expected a popup step")

    question = step.get("question", "")
    options = step.get("options", [])
    colors = step.get("colors", [])

    if len(options) != 3 or len(colors) != 3:
        return abort(400, description="Popup must have 3 options and 3 colors")

    options_colors = list(zip(options, colors))

    return render_template("popup_screen.html", question=question, options_colors=options_colors)


@screens.route("/screen/dropdown/<int:index>")
def screen_dropdown(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "dropdown":
        return abort(400, description="Expected a dropdown step")

    prompt = step.get("prompt", "Please select an option")
    options = step.get("options", [])


    return render_template("dropdown_screen.html", prompt=prompt, options=options)

@screens.route("/screen/text_input/<int:index>")
def screen_text_input(index):
    try:
        step = screen_config.flow_config[index]
    except IndexError:
        return abort(404, description="Invalid step index")

    if step.get("type") != "text_input":
        return abort(400, description="Expected a text_input step")

    return render_template("text_input.html", step=step)