# -*- coding: utf-8 -*-
import os

os.system("fswebcam /dev/video0 /home/pi/exercises/weather.jpg")

from slacker import Slacker

#OAuthToken
token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

slacker = Slacker(token)
channel_name = "#" + "general"
result = slacker.files.upload("/home/pi/exercises/weather.jpg",channels=["C016WF9UWN8"])
#slacker.chat.post_message("C016WF9UWN8", "That's the weather right now.", as_user=True)
slacker.pins.add(channel="C016WF9UWN8", file_=result.body["file"]["id"])
