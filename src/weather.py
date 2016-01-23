# -*- coding: utf-8 -*-
"""
Methods to obtain actual and predicted a place weather, using longitude and
latitude.
"""

##########
# IMPORT #
##########
import requests

#############
# FUNCTIONS #
#############
def actual_weather(latitude, longitude):
    """
    Return the weather at the location indicate at latitude/longitude.
    Return a dictionnary.
    """
    api_id = 'f88e4f9c0329490d11901f8ff47777df'

    latitude = str(latitude)
    longitude = str(longitude)

    web_data = requests.get("http://api.openweathermap.org/data/2.5/weather?lat="
                           + latitude +"&lon="+ longitude +
                           "&appid="+api_id).json()
    # weather.json() -> dico

    weather = {}
    weather["description"] = web_data['weather'][0]['description']
    weather["humidity (%)"] = web_data['main']['humidity']
    weather["wind (m/s)"] = web_data['wind']['speed']
    weather["temperature (°C)"] = kelvin_to_celsius(web_data['main']['temp'])

    print(weather)


def kelvin_to_celsius(kelvin):
    """
    Convert kelvin temperature to celsius.
    """
    return kelvin-273.15

actual_weather(46.5798114,0.34189)
