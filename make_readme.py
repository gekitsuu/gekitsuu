from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_environment():
    return Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())


def main():
    env = get_environment()
    template = env.get_template("source_readme.md")
    with open('README.md', '+rw') as fh:
        fh.write(template.render())


if __name__ == "__main__":
    main()