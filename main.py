from utils import active_astronauts_names, active_astronauts_count, names_emails, avg_by_pandas, requirements_info, \
    random_string, get_pass
from sqlite_pr import exec_query
from flask import Flask, request

app = Flask('app')


# "Меню" для навигации
def navi():
    page = '<a href="/">Home Page</a>&nbsp&nbsp' \
           '<br>HW-1:&nbsp' \
           '<a href="/requirements">Requirements</a>&nbsp&nbsp' \
           '<a href="/users">Users</a>&nbsp&nbsp' \
           '<a href="/average">Average</a>&nbsp&nbsp' \
           '<a href="/astronauts">Astronauts</a>&nbsp&nbsp' \
           '<br>HW-2:&nbsp' \
           '<a href="/all-customers">All Customers</a>&nbsp&nbsp' \
           '<a href="/customers-from-state-and-city?state=QC&city=Montréal">Customers by state and city</a>&nbsp&nbsp' \
           '<a href="/gen?len=20">String generator</a>&nbsp&nbsp' \
           '<a href="/customers-with-unique-names">Unique names</a>&nbsp&nbsp' \
           '<br><br>'
    return page


@app.route('/')
def hello():
    page = navi()
    page += 'Hello!'
    return page


# HW-1
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
    av = avg_by_pandas()
    page += f'Average height: {av["avg_height"]}<br>' \
            f'Average weight: {av["avg_weight"]}'
    return page


@app.route('/astronauts')
def astronauts():
    page = navi()
    page += f'Astronauts count: {active_astronauts_count()}<br><br>'
    page += active_astronauts_names()
    return page


@app.route('/all-customers')
def all_customers():
    page = navi()
    q = f'SELECT * FROM customers;'
    page += str(exec_query(q))
    return page


# HW-2
@app.route('/gen')
def gen():
    page = navi()
    page += get_pass(request.args["len"])
    return page


@app.route('/customers-from-state-and-city')
def customers_state_city():
    page = navi()
    # a = 'http://127.0.0.1:5000/all-customers?name=Dima&last-name='
    q = f'SELECT * FROM customers WHERE ' \
        f'state = "{request.args["state"]}" ' \
        f'and city = "{request.args["city"]}";'
    page += exec_query(q)
    return page


@app.route('/customers-with-unique-names')
def unique_names():
    page = navi()
    q = 'SELECT COUNT(DISTINCT FirstName) FROM customers;'
    page += str(exec_query(q))
    return page


if __name__ == '__main__':
    app.run(port=5000, debug=True)
