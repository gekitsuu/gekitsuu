import readme

env = readme.get_environment()

template = env.get_template("source_readme.md")
with open('README.md', '+rw') as fh:
    fh.write(template.render())