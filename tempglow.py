#Changed to F
#Use temp_c for C

import string
from PyGlow import PyGlow
from time import sleep
import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/0c3acb7d79bd4f22/geolookup/q/autoip.json')
json_string = f.read()
parsed_json = json.loads(json_string)
zip = parsed_json['location']['zip']

f = urllib2.urlopen('http://api.wunderground.com/api/0c3acb7d79bd4f22/geolookup/conditions/q/%s.json' % (zip))
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()

pyglow = PyGlow() #Setup piglow and turn all off
pyglow.all(0)
pyglow.all(brightness=255, speed=500, pulse=True)
sleep(1)
pyglow.all(brightness=255, speed=500, pulse=True)
sleep(1)
pyglow.all(brightness=255, speed=500, pulse=True)
sleep(1)

temperature=int(temp_f)
if temperature < 0:
   pyglow.color("blue", 255)
elif temperature < 10:
     pyglow.color("blue", 255)
     pyglow.color("green", 200)
elif temperature < 20:
     pyglow.color("green", 255)
     pyglow.color("blue", 255)
     pyglow.color("orange", 150)
     pyglow.color("yellow", 255)
elif temperature < 32:
     pyglow.color("green", 255)
     pyglow.color("blue", 120)
     pyglow.color("orange", 150)
     pyglow.color("yellow", 255)
elif temperature < 40:
     pyglow.color("green", 255)
     pyglow.color("yellow", 200)
     pyglow.color("orange", 210)
     pyglow.color("red", 200)
elif temperature < 50:
     pyglow.color("green", 240)
     pyglow.color("yellow", 200)
     pyglow.color("orange", 255)
     pyglow.color("red", 220)
elif temperature < 60:
     pyglow.color("green", 220)
     pyglow.color("yellow", 255)
     pyglow.color("orange", 255)
     pyglow.color("red", 255)
elif temperature < 70:
     pyglow.colur("green", 180)
     pyglow.color("yellow", 255)
     pyglow.color("orange", 255)
     pyglow.color("red", 255)
elif temperature < 80:
     pyglow.color("green", 90)
     pyglow.color("yellow", 255)
     pyglow.color("orange", 255)
     pyglow.color("red", 255)
elif temperature < 90:
     pyglow.color("red", 255)
     pyglow.color("orange", 255)
elif temperature < 100:
     pyglow.color("red", 255)
     pyglow.color("blue", 180)
     pyglow.color("orange", 255)
     pyglow.color("red", 255) 
else: pyglow.all(255)

	
