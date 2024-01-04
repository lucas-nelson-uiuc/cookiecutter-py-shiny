from shiny import ui
from htmltools._core import Tag


def base_template(
    header: str,
    description: str,
) -> Tag:
    """Base template for navigation bar help pages

    Parameters
    ----------
    header: str
        title on top of page
    description: str
        str to be converted to markdown
    """
    return ui.page_fluid(
        ui.h1(ui.tags.b(header), style="text-align: center;"),
        ui.hr(),
        ui.markdown(description),
        ui.hr(),
    )
