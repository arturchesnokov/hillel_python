from fake_name_email import names_emails
from astros import active_astronauts_names, active_astronauts_count
from flask import Flask

app = Flask('app')


@app.route('/')
def hello():
    return 'Hello'


@app.route('/requirements')
def requirements():
    with open('requirements.txt') as file:
        text = file.read()
    return "<br>".join(text.split("\n"))


@app.route('/users')
def users():
    return names_emails(100)


@app.route('/astronauts')
def astronauts():
    page = f'Astronauts count: {active_astronauts_count()}<br>'
    page += active_astronauts_names()
    return page


if __name__ == '__main__':
    app.run()
