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

schedule.every().day.at("18:10").do(jobUSA)

schedule.every().day.at("21:00").do(jobUSA)
schedule.every().day.at("21:15").do(jobUK)
schedule.every().day.at("21:30").do(jobCA)

while True:
    schedule.run_pending()
    time.sleep(1)