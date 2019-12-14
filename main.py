import random
import string

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


if __name__ == '__main__':
    app.run()
