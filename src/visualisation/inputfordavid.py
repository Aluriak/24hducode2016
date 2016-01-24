"""
Get text to put in little bubbles from the TObject container
"""

from TObject import TObject
from src import default


def get_information_from_tobject(tobject):
    """
    Get useful information from one TObject
    """
    return {'Latitude': TObject[default.FIELD_LATITUDE],
            'Longitude': TObject[default.FIELD_LONGITUDE],
            'Latitude': TObject[default.FIELD_NAME],
            }


def generate_lists_for_map(list):

