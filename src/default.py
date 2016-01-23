"""
Definitions of default values.

"""

FIELD_WEATHER_NOW = 'WeatherNow'  # dict {weaver data}
FIELD_WEATHER_PREDICTED = 'WeatherPredicted'  # dict {day number:{weaver data}}
FIELD_DATE = 'EventDate'  # datetime object

# Following fields are found in Events and Places
FIELD_NAME = 'ObjectName'  # String
FIELD_TYPE = 'Type'  # String
FIELD_UPDATED = 'Updated'  # Date
FIELD_GEOGRAPHY = 'Geography'  # Class containing all geograhpical data

# Following fields are found only in Places
FIELD_OPENING = 'OpeningTimes'  # Class containing time
FIELD_FREE = 'Free'  # Boolean to know if it's free

# Distinguish between an Event and a Place
FIELD_EVENT = 'Event'  # Boolean True if Event, False if Place

# Fields for Peter
FIELD_DESCRIPTION = 'description'
FIELD_URL = 'url'

