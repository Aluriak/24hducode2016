import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
from openweathermap_requests import OpenWeatherMapRequests

ow = OpenWeatherMapRequests(api_key='f88e4f9c0329490d11901f8ff47777df', cache_name='cache-openweathermap', expire_after=5*60)

# Historic weather by lat/lon

(lon, lat) = (0.34189, 46.5798114) # Poitiers

data = ow.get_weather(lon=lon, lat=lat)  # display current weather data
print(data)

