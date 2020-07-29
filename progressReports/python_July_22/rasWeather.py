# -*- coding: utf-8 -*-
import json
import datetime
import os
import requests
import sys

from pytz import timezone

API_KEY = 'da1bc6b2497e5f663ff00c738ed049f0'
ZIP = '965-0023,JP'
API_URL = 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'

def getWeatherForecast():
    weatherDescription=list.weather.main
    temperature = list.main.temp

    print("weather:{0}, temp:{1}".format( weatherDescription, temperature))

getWeatherForecast()
