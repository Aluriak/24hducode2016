"""
Get text to put in little bubbles from the TObject container
"""

from TObject import TObject
from src import default


def get_information_from_tobject(tobject):
    """
    Get useful information from one TObject
    """
    return {'latitude': TObject[default.FIELD_LATITUDE],
            'longitude': TObject[default.FIELD_LONGITUDE],
            'eventName': TObject[default.FIELD_NAME],
            }


def generate_lists_for_map(objectsList):
    latitudes = []
    longitudes = []
    text = []
    for tobject in objectsList:
        temp = get_information_from_tobject(tobject)
        latitudes.append(temp['latitude'])
        longitudes.append(temp['longitude'])
        text.append(temp['eventName'] + '\n')
    return [latitudes, longitudes, text]
