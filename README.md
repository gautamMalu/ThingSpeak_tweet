# ThingSpeak_tweet
This simple script uses Kaalu App on twitter to post tweet about current sensor value given channel number at https://thingspeak.com/

Publicly availabe channels  https://thingspeak.com/channels/public

For a private channel you have to also pass API key in url as
	url='http://api.thingspeak.com/channels/channel_number/feed.json?key="API_KEY"'

To post Tweets it uses Twython python library https://github.com/ryanmcgrath/twython 

To install twython via pip

$sudo pip install twython 


About Twitter api rate limit:
"For each update attempt, the update text is compared with the authenticating user’s recent tweets. Any attempt that would result in duplication will be blocked, resulting in a 403 error. Therefore, a user cannot submit the same status twice in a row."

More at https://dev.twitter.com/rest/reference/post/statuses/update


15 post request are allowed per 15 minutes.

More at https://dev.twitter.com/rest/public/rate-limiting



