import requests

BASE_EVENTS = ('http://wcf.tourinsoft.com/Syndication/3.0/cdt72/e9a8e2bf-' +
               'c933-4831-9ebb-87eec559a21a/')

BASE_PLACES = ('http://wcf.tourinsoft.com/Syndication/3.0/cdt72/969e24f9' +
               '-75a2-4cc6-a46c-db1f6ebbfe97/')

# FLAGS = 'format=json&metadata'
FLAGS = 'format=json'


def request():
    # r = requests.get(BASE_EVENTS + collection + '$' + FLAGS)
    r = requests.get(BASE_EVENTS + '$' + FLAGS)
    print(r.json())

request()
