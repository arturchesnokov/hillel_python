import requests
import json

REQUEST_URL = 'http://api.open-notify.org/astros.json'


def active_astronauts_count():
    r = requests.get(REQUEST_URL)
    people = json.loads(r.text)
    print(len(json.loads(r.text)["people"]))

    return len(people["people"])


def active_astronauts_names():
    r = requests.get(REQUEST_URL)
    people = json.loads(r.text)
    text = ''
    for astronaut in people['people']:
        text += astronaut['name'] + '<br>'
    return text


if __name__ == '__main__':
    print(active_astronauts_names(),'\n')
    active_astronauts_count()
