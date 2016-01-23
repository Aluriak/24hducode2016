import requests


# FLAGS = 'format=json&metadata'
FLAGS = 'format=json'

latitude = "0.34189"
longitude = "46.5798114"

def request():
    re = "http://api.openweathermap.org/data/2.5/forecast?lat="+ latitude +"&lon="+longitude+"&appid=f88e4f9c0329490d11901f8ff47777df"
    print(re)
    r = requests.get(re)
    #r = requests.get(BASE + str(latitude) + "&lon="+ str(longitude) +"&appid=f88e4f9c0329490d11901f8ff47777df")
    print(r.json())

request()
