import os
import time
import urllib2
import json
from twython import Twython

#proxy settings
os.environ['http_proxy'] = 'proxy.rolling_friction.in:8080'
os.environ['https_proxy'] = 'proxy.rolling_friction.in:8080'

# Consumer key aka API key for Kaalu app
APP_KEY = 'UghjDx0rzAvyJ5zBaFeUjj5Df'

#Consumer Secret aka API secret obtained from above given url
APP_SECRET = 'YKr17y6745UcFIzZBCLUPD7OPOXxfwDUMsxEksUcR1VuYLh9Xi'

#Getting auth tokens
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
url=auth['auth_url']
print 'open this in browser and authorize Kaalu app '+url
oauth_verifier = raw_input("Provide PIN Number: ")

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
final_step = twitter.get_authorized_tokens(oauth_verifier)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Getting channel number
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
        tweet = 'the current sensor value from channel '+str(chn)+' on thingspeak is '+str(sensor_value)
	print tweet
	twitter.update_status(status=tweet)
         



# Time intervals between consecutive tweets because of twitter API limit
# things speak API time limit is 15 seconds
time_interval = 15 
if __name__ == "__main__":
    while True:
        doit()
        time.sleep(time_interval*60) 
