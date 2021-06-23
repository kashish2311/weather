import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_des = api_data['weather'][0]['description']
hmd = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("|||||||||||||||")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("|||||||||||||||")

print ("Today's Temperature : {:.2f} C".format(temp_city))
print ("Weather des  :",weather_des)
print ("Humidity      :",hmd, '%')
print ("Wind Speed    :",wind_spd ,'kph')