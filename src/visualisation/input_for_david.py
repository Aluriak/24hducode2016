"""
Get text to put in little bubbles from the TObject container
"""

from tobject import TObject
import default


def get_information_from_tobject(tobject):
    """
    Get useful information from one TObject
    """
    return {'latitude': tobject[default.FIELD_LATITUDE],
            'longitude': tobject[default.FIELD_LONGITUDE],
            'eventName': tobject[default.FIELD_NAME],
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
