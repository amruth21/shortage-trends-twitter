from botV1 import *
from trends import *
import schedule
import time

print("Scheduler Running...")

def jobUSA():
    createTweet("United States")

def jobUK():
    createTweet("United Kingdom")

def jobCA():
    createTweet("Canada")

#Heroku servers 4 hours ahead
schedule.every().day.at("01:00").do(jobUSA) #Posts at 9:00pm EST
schedule.every().day.at("01:15").do(jobUK) #Posts at 9:05pm EST
schedule.every().day.at("01:30").do(jobCA) #Posts at 9:30pm EST

while True:
    schedule.run_pending()
    time.sleep(1)