import os
import time
import urllib2
import json
from twython import Twython
from pprint import pprint

# Consumer key aka API key for out beloved twitter named Kaalu
# Check it out from https://apps.twitter.com/app/7762678/keys
# dehati_aadmi has made this app/api so only he can access 
# the above given url
APP_KEY = 'UghjDx0rzAvyJ5zBaFeUjj5Df'

#Consumer Secret aka API secret obtained from above given url
APP_SECRET = 'YKr17y6745UcFIzZBCLUPD7OPOXxfwDUMsxEksUcR1VuYLh9Xi'

#following tokens are received once a user in this stance 
# dehati_aadmi authorize the access of app
OAUTH_TOKEN='2314028468-qPiUja96eCo1rFnvV6RBBAMszwhSBn0dpoPqwRz'
OAUTH_TOKEN_SECRET='ZPm29rJ8vTeafTQnfrtxpNfKMZlz90HU31XKFYqeM6THS'

#proxy settings
os.environ['http_proxy'] = 'proxy.rolling_friction.in:8080'
os.environ['https_proxy'] = 'proxy.rolling_friction.in:8080'


# Creating a instance of twitter from above given info
twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
chn = raw_input("Give Channel Number: ")

def doit():
	# Data coming from given public channel in json format
	# for private channel use your API key with ?key="API KEY"
	
	url='http://api.thingspeak.com/channels/'+str(chn)+'/feed.json'
	response = urllib2.urlopen(url)
	html = response.read()
	json_data = json.loads(html)
	# Get the size of the array so that we could select the lastest lastest value 
	n_f=len(json_data["feeds"])
        sensor_value = json_data["feeds"][n_f-1]["field1"] # getting data from field1 only
        tweet = 'the current sensor value from channel 22764 on thingsspeak is '+str(sensor_value)
	print tweet
	twitter.update_status(status=tweet)
         



# Time intervals between consecutive tweets because of twitter API limit
# things speak API time limit is 15 seconds
time_interval = 15 
if __name__ == "__main__":
    while True:
        doit()
        time.sleep(time_interval*60) 
