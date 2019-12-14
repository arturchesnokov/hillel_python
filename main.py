from fake_name_email import names_emails
from astros import active_astronauts_names, active_astronauts_count
from read_csv import avg_height_weight
from requirements_read import requirements_info
from flask import Flask

app = Flask('app')


def navi():
    page = '<a href="/">Home Page</a>&nbsp&nbsp' \
           '<a href="/requirements">Requirements</a>&nbsp&nbsp' \
           '<a href="/users">Users</a>&nbsp&nbsp' \
           '<a href="/average">Average</a>&nbsp&nbsp' \
           '<a href="/astronauts">Astronauts</a>&nbsp&nbsp' \
           '<br><br>'
    return page


@app.route('/')
def hello():
    page = navi()
    page += 'Hello!'
    return page


@app.route('/requirements')
def requirements():
    page = navi()
    page += requirements_info()
    return page


@app.route('/users')
def users():
    page = navi()
    page += names_emails(100)
    return page


@app.route('/average')
def average():
    page = navi()
    av = avg_height_weight()
    page += f'Average height: {av["avg_height"]}<br>' \
            f'Average weight: {av["avg_weight"]}'
    return page


@app.route('/astronauts')
def astronauts():
    page = navi()
    page += f'Astronauts count: {active_astronauts_count()}<br><br>'
    page += active_astronauts_names()
    return page


if __name__ == '__main__':
    app.run()
