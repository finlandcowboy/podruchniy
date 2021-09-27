from bot import send_weather
from bs4 import BeautifulSoup
import requests
import json
api_key = '6cf90f02172365e26bd055da73305fe3'
#requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}')
city = 'Moscow'

weather_json_data = json.loads(requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').text)

