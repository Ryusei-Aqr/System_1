import os

os.system("fswebcam /dev/video0 weather.jpg")

from slacker import Slacker

#OAuthToken
token = "xoxp-1234430567092-1213507232231-1228269505394-0a816f3d41448d3ff85fdcecb14c7e00"

slacker = Slacker(token)
channel_name = "#" + "general"
result = slacker.files.upload("/home/pi/ex8/weather.jpg",channels=["C016WF9UWN8"])
slacker.chat.post_message("C016WF9UWN8", "That's the weather right now.", as_user=True)
slacker.pins.add(channel="C016WF9UWN8", file_=result.body["file"]["id"])
