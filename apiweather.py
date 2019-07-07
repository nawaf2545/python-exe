import requests

api_adderess = 'https://samples.openweathermap.org/data/2.5/weather?id=2172797&appid=b6907d289e10d714a6e88b30761fae22'
city = input("please enter city")
url = api_adderess + city
data = requests.get(url).json()
print(data)