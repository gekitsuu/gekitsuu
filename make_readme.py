import datetime
import subprocess

from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_environment():
    return Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

def get_manpage(env):
    template = env.get_template("manpage.md")
    template.globals['datetime'] = datetime
 
    with open('rendered_manpage.md', '+w') as fh:
        fh.write(template.render())
    
    subprocess.check_output('pandoc rendered_manpage.md -s -t man -o gekitsuu.1', shell=True)
    rendered_manpage = subprocess.check_output('MANWIDTH=80 man -l gekitsuu.1|cat', shell=True)

    return rendered_manpage

def main():
    env = get_environment()
    template = env.get_template("readme.md")
    template.globals['manpage'] = bytearray(get_manpage(env)).decode()
    with open('README.md', '+w') as fh:
        fh.write(template.render())


if __name__ == "__main__":
    main()