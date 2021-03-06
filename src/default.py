"""
Definitions of default values.

"""

from datetime import datetime
from functools import partial

# CONSTANTS
SUBMODULES_SOURCES_PREFIX = 'sources_'
ALL_DATA_FILE = 'ressources/tobjects.pkl'


# FIELDS OF TOBJECTS
FIELD_WEATHER_NOW = 'WeatherNow'  # dict {weaver data}
FIELD_WEATHER_PREDICTED = 'WeatherPredicted'  # dict {day number:{weaver data}}
FIELD_DATE = 'EventDate'  # datetime object

# Following fields are found in Events and Places
FIELD_ID = 'object_id'  # String
FIELD_NAME = 'object_name'  # String
FIELD_TYPE = 'type'  # String
FIELD_UPDATED = 'updated'  # Date
FIELD_LATITUDE = 'latitude'  # Class containing all geograhpical data
FIELD_LONGITUDE = 'longitude'  # Class containing all geograhpical data
FIELD_CITY = 'city'
FIELD_ZIPCODE = 'zipcode'

# Following fields are found only in Places
FIELD_OPENING = 'opening_times'  # Class containing time
FIELD_FREE = 'free'  # Boolean to know if it's free

# Distinguish between an Event and a Place
FIELD_EVENT = 'event'  # Boolean True if Event, False if Place

# Fields for Peter
FIELD_DESCRIPTION = 'description'
FIELD_URL = 'url'

# Types definition
TOURINFO_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'


def date_type_wrapped(string, format):
    """Wrapper around datetime, allowing usage of keywords arguments"""
    if '.' in string:
        string = string.split('.')[0]
    return datetime.strptime(string, format)

date_type = partial(date_type_wrapped, format=TOURINFO_DATE_FORMAT)
