#Utilizes Twitter API v2 requires Essential Access
#Note cannot upload new Images with v2 API only preexisting media IDs

import tweepy
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")
print(config)

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=config['consumer_key'], consumer_secret=config['consumer_secret'],
    access_token=config['access_token'], access_token_secret=config['access_token_secret']
)

response = client.create_tweet(
    text="test"
)

media = client.media_upload("Cat03.jpg")
 
# Post tweet with image
post_result = client.create_tweet(text="testing image", media_ids=[media.media_id])
 
