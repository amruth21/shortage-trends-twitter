#Utilizes Twitter API v1 requires Elevated Access

import tweepy
from trends import *
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")

consumer_key = config['consumer_key'] 
consumer_secret = config['consumer_secret']

bearer_token = config['bearer_token'] 

access_token = config['access_token'] 
access_token_secret = config['access_token_secret'] 

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

#Place ID
place = api.search_geo(query="United States", granularity="country")
placeID = place[0].id

#Generate Media ID from PIL Image
graph = pullData()
b = io.BytesIO()
graph.save(b, "PNG")
b.seek(0)
fp = io.BufferedReader(b)
graph.show()
media = api.media_upload(filename="not applicable", file=fp)

#Create Tweet
tweet = "Testing PLT"
api.update_status(status=tweet, media_ids=[media.media_id], place_id=placeID)

print(api.verify_credentials().screen_name)

