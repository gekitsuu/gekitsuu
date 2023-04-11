import readme

env = readme.get_environment()

template = env.get_template("source_readme.md")
print(template.render())
