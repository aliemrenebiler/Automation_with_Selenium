"Jinja Utils"

from jinja2 import Environment, FileSystemLoader


def create_html_from_jinja_template(
    template_folder_path: str,
    template_file_name: str,
    template_variables: dict,
) -> str:
    "Creates HTML from Jinja template"

    environment = Environment(loader=FileSystemLoader(template_folder_path))
    template = environment.get_template(template_file_name)
    html = template.render(**template_variables)
    return html
