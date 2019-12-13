import random
import string

from flask import Flask

app = Flask('app')


@app.route('/')
def hello():
    return 'Hello'


@app.route('/hello-world')
def hello_world():
    return 'Hello world'


@app.route('/gen')
def gen():
    return ''.join(
        random.choice(string.ascii_uppercase) for i in range(10)
    )


if __name__ == '__main__':
    app.run()

# Faker
# request
# pandas
