# -*- coding: utf-8 -*-
import json
import datetime
import os
import requests
import sys

from pytz import timezone

API_KEY = 'xxxxxxxxxx'
ZIP = 'xxx-xxxx,JP'
API_URL = 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'

def getWeatherForecast():
    weatherDescription=list.weather.main
    temperature = list.main.temp

    print("weather:{0}, temp:{1}".format( weatherDescription, temperature))

getWeatherForecast()
