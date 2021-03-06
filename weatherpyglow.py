import string
from PyGlow import PyGlow
from time import sleep
import urllib2
import json

# get <your API key> from http://www.wunderground.com/weather/api 
f = urllib2.urlopen('http://api.wunderground.com/api/<your API key>/geolookup/q/autoip.json')
json_string = f.read()
parsed_json = json.loads(json_string)
zip = parsed_json['location']['zip']

f = urllib2.urlopen('http://api.wunderground.com/api/<your API key>/geolookup/conditions/q/%s.json' % (zip))
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
weather = parsed_json['current_observation']['weather']
print "Current weather in %s is: %s" % (location, weather)
f.close()

weather = string.lower(weather)
pyglow = PyGlow() #Setup piglow and turn all off
pyglow.all(0)

if weather in ["partly cloudy", "mostly cloudy", "cloudy", "overcast", "scattered clouds"]: 
    pyglow.color("white", 150)
     
elif weather in ["mixed rain and snow" , "mixed snow and sleet" , "freezing drizzle" , "freezing rain" , "snow flurries" , "light snow showers" , "blowing snow" , "snow" , "hail" , "sleet" , "dust" , "heavy snow" , "scattered snow showers" , "snow showers" , "light snow", "light snow grains"]:
    pyglow.color("yellow", 150)	

elif weather in ["severe thunderstorms", "thunderstorms", "isolated thunderstorms" , "scattered thunderstorms" , "thundershowers"]:
    pyglow.color("red", brightness=150, speed=4000, pulse=True)

elif weather in ["mixed rain and sleet" , "drizzle" , "showers" , "scattered showers" , "mixed rain and hail" , "rain"] :
    pyglow.color("blue", 150)
	
elif weather in ["windy" , "cold"]:
    pyglow.color("blue", 150)
    pyglow.color("red", 150)	

elif weather in ["clear" , "hot" , "sunny" , "fair"]:
    pyglow.color("green", 150)
	
elif weather in ["fog" , "foggy" , "haze" , "smokey" , "blustery"] : 
    pyglow.color("blue", 200)
    pyglow.color("white", 150)
 
else:
    pyglow.all(1)

		
				

		
