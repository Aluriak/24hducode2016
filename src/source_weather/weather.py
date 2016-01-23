# -*- coding: utf-8 -*-
"""
Methods to obtain actual and predicted a place weather, using longitude and
latitude.
"""

##########
# IMPORT #
##########
import datetime
import requests

#############
# FUNCTIONS #
#############
def actual(latitude, longitude):
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
    # web_data.json() -> dico

    weather = {}
    weather["description"] = web_data['weather'][0]['description']
    weather["humidity (%)"] = web_data['main']['humidity']
    weather["wind (km/h)"] = round(mps_to_kmph(web_data['wind']['speed']),2)
    weather["temperature (°C)"] = round(kelvin_to_celsius(web_data['main']['temp']),2)

    return weather

def predicted(latitude, longitude):
    """
    Return the predicted weather for the next 5 days.
    """
    api_id = 'f88e4f9c0329490d11901f8ff47777df'

    latitude = str(latitude)
    longitude = str(longitude)

    web_data = requests.get("http://api.openweathermap.org/data/2.5/forecast?lat="
                           + latitude +"&lon="+ longitude +
                           "&appid="+api_id).json()['list']
    predicted_weather = {}
    for day in web_data:
        if day['dt_txt'][-8:] == "15:00:00":
            predicted_weather[day['dt_txt'][:10]] = {
                'description': day['weather'][0]['description'],
                'humidity (%)': day['main']['humidity'],
                "wind (km/h)": round(mps_to_kmph(day['wind']["speed"]),2),
                "temperature (°C)": round(kelvin_to_celsius(day['main']['temp']),2)}
    return predicted_weather


def kelvin_to_celsius(kelvin):
    """
    Convert kelvin temperature to celsius.
    """
    return kelvin-273.15

def mps_to_kmph(mps):
    """
    Convert meter/s to km/h
    """
    return mps*3.6

def is_predictable(request):
    """
    Check if at the date, the weather can be predict.
    Output: boolean
    """
    today = datetime.date.today()
    if request.toordinal() - today.toordinal() >= 5:
        return True
    else:
        return False


#predicted(46.5798114,0.34189)
