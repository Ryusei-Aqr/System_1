# -*- coding: utf-8 -*-
import json
import datetime
import os
import requests
import sys

from pytz import timezone
from slacker import Slacker

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxx'
city = "kitakata"
API_URL = 'http://api.openweathermap.org/data/2.5/weather?'
makeUrl = API_URL + "appid=" + API_KEY + "&q=" + city
response = requests.get(makeUrl)
cityData = response.json()

#For Slack
token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

slacker = Slacker(token)
channel_name = "#" + "general"

# Codが404だと都市名が見つかりませんの意味
if cityData["cod"] != "404":
        slacker.chat.post_message("C016WF9UWN8", "Current Weather:", as_user=True)
        slacker.chat.post_message("C016WF9UWN8", cityData["weather"][0]["description"] ,as_user=True)
        slacker.chat.post_message("C016WF9UWN8", "Current Temperature(℃)", as_user=True)
        slacker.chat.post_message("C016WF9UWN8", round(cityData["main"]["temp"] - 273.15,1), as_user=True)
        slacker.chat.post_message("C016WF9UWN8", "Maximum Temperature(℃)", as_user=True)
        slacker.chat.post_message("C016WF9UWN8", round(cityData["main"]["temp_max"] - 273.15,1), as_user=True)
        slacker.chat.post_message("C016WF9UWN8", "Minimum Temperature(℃)", as_user=True)
        slacker.chat.post_message("C016WF9UWN8", round(cityData["main"]["temp_max"] - 273.15,1), as_user=True)
        slacker.chat.post_message("C016WF9UWN8", "Humidity", as_user=True)
        slacker.chat.post_message("C016WF9UWN8", cityData["main"]["humidity"], as_user=True)
        slacker.chat.post_message("C016WF9UWN8", "Wind Speed", as_user=True)
        slacker.chat.post_message("C016WF9UWN8", cityData["wind"]["speed"], as_user=True)
        slacker.chat.post_message("C016WF9UWN8", "---------------------------------------", as_user=True)
else: 
	print("都市名がみつかりませんでした。") 
