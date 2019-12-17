from faker import Faker
import pandas
import requests
import json
import os
import random
import string


# generator of pass string
def random_string(qty) -> str:
    return ''.join(
        random.choice(string.ascii_uppercase) for i in range(qty)
    )


# verify len-param and returns password or message
def get_pass(length) -> str:
    if length:
        try:
            pass_len = int(length)
            if 6 <= pass_len <= 1000:
                text = random_string(pass_len)
            else:
                text = "Length should be in range from 6 to 1000"
        except ValueError:
            text = "Length value should be integer"
    else:
        text = f"Default length(10) password:<br>{random_string(10)}"
    return text


def requirements_info() -> str:
    req_path = os.path.join(os.getcwd(), 'requirements.txt')
    with open(req_path) as file:
        text = file.read()
    return "<br>".join(text.split("\n"))


def names_emails(count) -> str:
    fake = Faker()
    user_list = ""
    for i in range(count):
        email = fake.email()
        user_list += fake.name() + ': <a href="mailto:' + email + '">' + email + '</a><br>'
    return user_list


FILE = 'hw.csv'


def avg_by_pandas(data_file=FILE) -> dict:
    df = pandas.read_csv(data_file, sep=',')
    h = df[' "Height(Inches)"'].mean()
    w = df[' "Weight(Pounds)"'].mean()
    return {"avg_height": h, "avg_weight": w}


REQUEST_URL = 'http://api.open-notify.org/astros.json'


def active_astronauts_count() -> int:
    r = requests.get(REQUEST_URL)
    people = json.loads(r.text)
    return len(people["people"])


def active_astronauts_names() -> str:
    r = requests.get(REQUEST_URL)
    people = json.loads(r.text)
    text = ''
    for astronaut in people['people']:
        text += astronaut['name'] + '<br>'
    return text


if __name__ == '__main__':
    print(active_astronauts_names(), '\n')
    print(active_astronauts_count())

    print(avg_by_pandas())
    print(names_emails(5))
