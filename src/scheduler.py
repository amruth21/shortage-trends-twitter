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
schedule.every().day.at("23:00").do(jobUSA) #Posts at 7:00pm EST
schedule.every().day.at("23:15").do(jobUK) #Posts at 7:15pm EST
schedule.every().day.at("23:30").do(jobCA) #Posts at 7:30pm EST

while True:
    schedule.run_pending()
    time.sleep(1)
