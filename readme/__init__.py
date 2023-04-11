from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_environment():
    return Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())