"""
This module contains tools used to parse the JSON dictionary output obtained
from a request on tourinsoft's API.
"""


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

    return(flattenedDictionary)


# Usage example
# test = flatten_dictionary({"a": 1, "b": {"c": 1, "d": 2}})
