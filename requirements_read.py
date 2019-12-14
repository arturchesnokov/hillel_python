def requirements_info():
    with open('requirements.txt') as file:
        text = file.read()
    return "<br>".join(text.split("\n"))