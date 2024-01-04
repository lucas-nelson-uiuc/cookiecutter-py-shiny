# cookiecutter-py-shiny: A cookiecutter template for `Shiny for Python` packages

[![python](https://img.shields.io/badge/python-%5E3.8-blue)]()
[![os](https://img.shields.io/badge/OS-Ubuntu%2C%20Mac%2C%20Windows-purple)]()

<br>

`cookiecutter-py-shiny` is a [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template for creating an elementary [Shiny for Python](https://shiny.posit.co/py/) package using [`poetry`](https://python-poetry.org). It is a clone of the cookiecutter template developed in the [Python Packages book](https://py-pkgs.org) by Tomas Beuzen and Tiffany Timbers but can be used independently.

## Usage

> **Note**: Please read the [Usage](https://github.com/py-pkgs/py-pkgs-cookiecutter#usage) section in the original cookiecutter's repository to learn more about the Python-package-specific features included.

Developing a Shiny application is a great experiences. Shiny lends itself to being a rapid development framework; however, due to my own messiness, I often find myself spending time recreating UI components or copying files/folders from other projects I've developed. Hence, it was obvious to make a `cookiecutter` template dedicated for Shiny projects in Python.

If interested, please follow the steps below to create your own `Shiny for Python` project. If the default project template does not meet your needs, feel free to fork your own copy and make the necessary edits. This will be an ongoing project, so check back in for updates in the future.

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

    ```bash
    pip install cookiecutter
    ```

2. Generate a Python package structure using [`cookiecutter-py-shiny`](https://github.com/lucas-nelson-uiuc/cookiecutter-py-shiny.git):

    ```bash
    cookiecutter https://github.com/lucas-nelson-uiuc/cookiecutter-py-shiny.git
    ```

3. After responding to the prompts you should have a directory structure similar to that shown below. To learn more about the contents of this directory structure, please see the `py-pkgs-cookiecutter` [documentation](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/).

    ```text
    pkg
    ... package docs, GitHub workflows ...
    ├── src                        ┐
    │   └── pkg                    │ Package source code, metadata,
    │       ├── __init__.py        │ and build instructions 
    │       └── pkg.py             |
    │       └── templates          | UI components
    │           └── icons.py       |
    │           └── pages          |
    │       └── modules            ┘ Server modules
    ... package tests ...
    ```

## Features

*in progress*

## Acknowledgements

Thank you to the work of Tomas, Tiffany, Daniel, and DC, the lead contributors of the [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter) template that this is built on top of. All credit from a packaging perspective should be geared towards them.

Thank you to [`Shiny for Python`](https://github.com/posit-dev/py-shiny) as well for being this beautiful framework I've grown close with over the years. All credit from a web application perspective should be geared towards the wonderful folks on Posit's Shiny team.
