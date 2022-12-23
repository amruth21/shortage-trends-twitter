#Utilizes Twitter API v1 requires Elevated Access
#Can create new media ID's used OAuth1
import os
import tweepy
from trends import *
from datetime import date
from dotenv import load_dotenv, dotenv_values

config = dotenv_values(".env")

if not os.environ.get("PRODUCTION"): #loads from env file
    consumer_key = config['consumer_key'] 
    consumer_secret = config['consumer_secret']

    access_token = config['access_token'] 
    access_token_secret = config['access_token_secret'] 

    bearer_token = config['bearer_token']
else: # loads from OS env var set by Heroku
    consumer_key = os.environ['consumer_key'] 
    consumer_secret = os.environ['consumer_secret']

    access_token = os.environ['access_token'] 
    access_token_secret = os.environ['access_token_secret'] 

    bearer_token = os.environ['bearer_token']


#Authentication
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

#Set up Methods
def setProfilePic(api, path):
    api.update_profile_image(filename=path)

def setBannerPic(api, path):
    api.update_profile_banner(filename=path)

#Generate Media ID from PIL Image
def generateID(graph):
    b = io.BytesIO()
    graph.save(b, "PNG")
    b.seek(0)
    fp = io.BufferedReader(b)
    #graph.show()
    return api.media_upload(filename="not applicable", file=fp)

def grabLocation(geo):
    place = api.search_geo(query=geo, granularity="country")
    placeID = place[0].id
    return placeID

def createTweet(geo):
    placeID = grabLocation(geo)

    if(geo == "United States"):
        arr = pullData("US")
        location = "USA"
        tweet = "𝐓𝐨𝐩 𝐒𝐡𝐨𝐫𝐭𝐚𝐠𝐞𝐬 𝐢𝐧 𝐔𝐒𝐀"

    if(geo == "India"):
        arr = pullData("IN")
        location = "India"
        tweet = "𝐓𝐨𝐩 𝐒𝐡𝐨𝐫𝐭𝐚𝐠𝐞𝐬 𝐢𝐧 𝐈𝐧𝐝𝐢𝐚"

    if(geo == "Canada"):
        arr = pullData("CA")
        location = "CA"
        tweet = "𝐓𝐨𝐩 𝐒𝐡𝐨𝐫𝐭𝐚𝐠𝐞𝐬 𝐢𝐧 𝐂𝐚𝐧𝐚𝐝𝐚"
    
    if(geo == "United Kingdom"):
        placeID = "6416b8512febefc9"
        location = "UK"
        arr = pullData("GB")
        tweet = "𝐓𝐨𝐩 𝐒𝐡𝐨𝐫𝐭𝐚𝐠𝐞𝐬 𝐢𝐧 𝐔𝐧𝐢𝐭𝐞𝐝 𝐊𝐢𝐧𝐠𝐝𝐨𝐦"


    #Create Tweet
    topTen = (arr['query'].to_numpy()[0:10])
    hashtag = ""
    hashtag += "#" + location + " "

    for i, y in enumerate(topTen):
        x = y.replace(" shortage", '')
        if(i < 3):
            hashtag += "#" + x + " "
        tweet += "\n" + str(i+1) + ". " + x

    tweet += "\n" + "Source: Google Trends for " + str(date.today())
    tweet += "\n" + hashtag

    
    #Generate graphs
    bar = generateID(barChart(arr)).media_id
    pie = generateID(pieChart(arr)).media_id
    bubble = generateID(bubblePlot(arr)).media_id
    
    api.update_status(status=tweet, media_ids=[bar, pie, bubble], place_id=placeID)


        
    