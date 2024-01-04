from shiny import App, Inputs, Outputs, Session, render, ui, run_app, reactive
from htmltools._core import Tag
import shinyswatch

from templates.icons import QUESTION_CIRCLE_FILL
from templates.pages.navbar_help import (
    contact_the_team
)

PACKAGE_NAME = {{ cookiecutter.package_name }}
app_ui = ui.page_navbar(
    [
        ui.nav_panel('Home', ui.page_fluid('something')),
        ui.nav_panel('Home2', ui.page_fluid('something')),
        ui.nav_spacer(),
        ui.nav_menu(
            'Help',
            'Navigation',
            ui.nav_panel(f'About { PACKAGE_NAME }', ui.page_fluid('inspiration from Polars homepage')),
            ui.nav_panel('User Guide', ui.page_fluid('inspiration from Polars')),
            ui.nav_panel('Frequently Asked Questions', ui.page_fluid('')),
            '-----',
            'Release Notes',
            ui.nav_panel('Changelog', ui.page_fluid('include upcoming changes')),
            ui.nav_panel('Looking to Contribute?', ui.page_fluid('inspiration from Polars, bslib')),
            '-----',
            'Additional Resources',
            ui.nav_panel('Contact the Team', contact_the_team.page_contact_the_team()),
            ui.nav_panel('Submit an Issue', ui.page_fluid('...')),
            icon=QUESTION_CIRCLE_FILL,
            align='right'
        )
    ],
    shinyswatch.get_theme(PACKAGE_NAME),
    title=PACKAGE_NAME,
    fluid=True,
    position='static-top'
)

def server(input: Inputs, output: Outputs, session: Session):
    pass


app = App(ui=app_ui, server=server)

if __name__ == '__main__':
    run_app(app)
