def requirements_info() -> str:
    with open('requirements.txt') as file:
        text = file.read()
    return "<br>".join(text.split("\n"))
