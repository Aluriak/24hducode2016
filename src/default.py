"""
Definitions of default values.

"""


# CONSTANTS
SUBMODULES_SOURCES_PREFIX = 'sources_'


# FIELDS OF TOBJECTS
FIELD_WEATHER_NOW = 'WeatherNow'  # dict {weaver data}
FIELD_WEATHER_PREDICTED = 'WeatherPredicted'  # dict {day number:{weaver data}}
FIELD_DATE = 'EventDate'  # datetime object

# Following fields are found in Events and Places
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
