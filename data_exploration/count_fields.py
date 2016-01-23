import requests
from collections import Counter

"""
Example of request function to be used on tourinsoft API
Input : base (events or places)

"""

URL = 'http://wcf.tourinsoft.com/Syndication/3.0/cdt72/'

EVENT_URL = 'e9a8e2bf-c933-4831-9ebb-87eec559a21a/'

PLACES_URL = '969e24f9-75a2-4cc6-a46c-db1f6ebbfe97/'

# Parameters are stored as a dictionary
parameters = {}


def request(collection, parameters={}, metadata=True, event=True):
    param_str = ('&' + par + '=' + parameters[par] for par in parameters)
    url = URL + ''.join((EVENT_URL if event else PLACES_URL,
                        collection,
                         '?$format=json',
                         ''.join(param_str),
                         '&metadata' if metadata else ''))
    return requests.get(url).json()['value']

events = request('Objects')
places = request('Objects', event=False)


def gendata(events):
    for tobject in events:
        for key, value in tobject.items():
            if isinstance(value, dict):
                for subkey in value.keys():
                    yield key + '.' + subkey
            else:
                yield key


def count_values(events):
    from collections import defaultdict
    c = defaultdict(Counter)
    for tobject in events:
        for key, value in tobject.items():
            if isinstance(value, dict):
                for subkey, subvalue in value.items():
                    c[key + '.' + subkey][subvalue] += 1
            else:
                c[key][value] += 1
    return c

c = Counter(gendata(events))
d = Counter(gendata(places))

print(c + d)
