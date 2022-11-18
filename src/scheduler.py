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

schedule.every().day.at("7:00").do(jobUSA) #Posts at 3:00am EST
schedule.every().day.at("7:15").do(jobUK) #Posts at 3:15am EST
schedule.every().day.at("7:30").do(jobCA) #Posts at 3:30am EST

schedule.every().day.at("15:00").do(jobUSA) #Posts at 11:00am EST
schedule.every().day.at("15:15").do(jobUK) #Posts at 11:15am EST
schedule.every().day.at("15:30").do(jobCA) #Posts at 11:30am EST

while True:
    schedule.run_pending()
    time.sleep(1)
