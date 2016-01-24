"""
This module contains tools used to get data using tourinsoft's API.
Request outputs JSON which is converted to a dictionary.
"""

import requests


URL = 'http://wcf.tourinsoft.com/Syndication/3.0/cdt72/'
EVENT_URL = 'e9a8e2bf-c933-4831-9ebb-87eec559a21a/'
PLACES_URL = '969e24f9-75a2-4cc6-a46c-db1f6ebbfe97/'


# shortcuts
def request_places():
    return request(event=False)
def request_events():
    return request(event=True)


def flatten_dictionary(dictionary):
    """
    Input: a request's JSON dictionary output with nested dictionary
    Output: a flattened dictionary (format: key1.key2 = value2)
    """
    flattenedDictionary = dict()
    for key, value in dictionary.items():
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                flattenedDictionary[key + '.' + subkey] = subvalue
        else:
            flattenedDictionary[key] = value
    return flattenedDictionary


def request(collection='Objects', parameters=dict(), metadata=True,
            event=True):
    """
    General request function.
    Input:
        - collection: general API folder (Objects contains events + places)
        - parameters: dictionary of parameters (useless)
        - metadata: boolean to get metadata instead of values
          (doesn't seem to matter in practice)
        - event: search in events DB (if False, will search in places DB)
    Output: a tuple of dictionaries (one dictionary for one object) containing
    the properties of each object.
    """
    param_str = ('&' + par + '=' + parameters[par] for par in parameters)
    url = URL + ''.join((EVENT_URL if event else PLACES_URL,
                        collection,
                        '?$format=json',
                         ''.join(param_str),
                         '&metadata' if metadata else ''))
    # Values field contains a list of all objects (other fields are useless)
    # Flatten dictionary formats nested dictionaries (see module parser)
    jsonOutput = requests.get(url).json()['value']
    return tuple(flatten_dictionary(tobject) for tobject in jsonOutput)

# Usage example
# test = request()
