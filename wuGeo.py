#Finds current location and displays temperature (in F)
 
import urllib2
import json

#Use geolookup to find current location by zip code
f = urllib2.urlopen('http://api.wunderground.com/api/<your_api_key>/geolookup/q/autoip.json')
json_string = f.read()
parsed_json = json.loads(json_string)
zip = parsed_json['location']['zip']

#Use the zip code to find the current conditions
f = urllib2.urlopen('http://api.wunderground.com/api/<your_api_key>/geolookup/conditions/q/%s.json' % (zip))
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
#Extract the current temperature in F 
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()

