from .base_navbar_help import base_template
from shiny import ui


def page_contact_the_team():
    return ui.page_fluid(
        base_template(
            header="Contact the Team",
            description="""
            Contact the team...
            """
        )
    )
