JTBrix
======

.. image:: https://img.shields.io/pypi/v/JTBrix.svg
    :target: https://pypi.python.org/pypi/JTBrix


.. image:: https://readthedocs.org/projects/JTBrix/badge/?version=latest
    :target: https://JTBrix.readthedocs.io/en/latest/?version=latest
    :alt: Documentation Status

![CI](https://github.com/amidn/JTBrix/workflows/CI/badge.svg?branch=main)

JTBrix is a modular Python package for running customizable video-based behavioral experiments in psychology and cognitive science.  
It supports full-screen playback, flexible configuration via YAML, conditional logic flows, and detailed logging of user responses and timing.

* Free software: MIT license
* Documentation: https://JTBrix.readthedocs.io

Features
--------

* Dynamically configurable experiments using a `config.yml` file.
* Supports multiple step types: consent, video, question, popup, dropdown, and end screens.
* Records answers and reaction times per screen.
* Fullscreen iframe-based flow in a single browser tab.
* Video and image stimuli loaded from a customizable static directory.
* Modular design for extension and easy deployment via Flask.

Installation
------------

You can install JTBrix via pip:

.. code-block:: bash

    pip install JTBrix

Command-line Usage
------------------

You can also run JTBrix directly via the command-line using Typer:

.. code-block:: bash

    typer src/JTBrix/cli.py run

or

.. code-block:: bash

    python src/JTBrix/cli.py

To enable shell autocompletion:

.. code-block:: bash

    typer --install-completion

Usage
-----

Basic example of how to start an experiment:

.. code-block:: bash

    typer src/JTBrix/cli.py run
    

By default, JTBrix looks for a configuration file (`config.yml`) and a `static/` folder under the `Data/` directory.

After running an experiment, the results are automatically saved in multiple formats—TXT, JSON, YAML, and CSV—under the `src/JTBrix/data/results/` folder.

You can find and modify the configuration settings of your experiment in the `src/JTBrix/data/` directory. This includes the `config.yml` file and any associated media content needed for stimuli.

The `static/` folder must include two subfolders:

- `videos/` – for video stimuli (e.g., `.mp4` files)  
- `images/` – for images used in questions (e.g., `.jpeg`, `.png`)

You can place these folders anywhere locally or on a server and provide the paths explicitly when calling `run_test()`.

YAML Configuration Structure
----------------------------

The experiment is defined in a YAML file (`config.yml`) located in `src/JTBrix/data/`.

- The configuration contains a list called `experiment_content` with multiple blocks.
- Each block starts with a tag:
  - `"Begin"`: always shown first, only once.
  - `"end"`: always shown last, only once.
  - Blocks with `"SetCode"`: randomized before the experiment starts.

- Inside each block are step definitions with a `type` key:
  - `type: "video"` → plays a video using `video_filename`
  - `type: "question"` → presents a question with options and optional image
  - `type: "popup"` → asks for confidence or follow-up response
  - `type: "text_input"`, `dob`, `dropdown` → collects user info

⚠️ YAML spacing is strict:
- Use `- -` (dash + space + dash) for nested steps.
- Avoid writing `--`, which is invalid syntax.

Credits
-------

JTBrix was designed and developed by Amid Nayerhoda for experimental research in cognitive science and psychology.
