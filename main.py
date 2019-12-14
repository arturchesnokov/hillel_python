import random
import string

from flask import Flask

app = Flask('app')


@app.route('/')
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run()
