"Jinja Utils"

from jinja2 import Environment, FileSystemLoader

from models.errors import JinjaError


def create_html_from_jinja_template(
    template_folder_path: str,
    template_file_name: str,
    template_variables: dict,
) -> str:
    "Creates HTML from Jinja template"

    try:
        environment = Environment(loader=FileSystemLoader(template_folder_path))
        template = environment.get_template(template_file_name)
        html = template.render(**template_variables)
    except Exception as exc:
        raise JinjaError(str(exc)) from exc
    return html
