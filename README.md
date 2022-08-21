# shortage-trends-twitter
A twitter bot programmed using Python3 to fetch and post Shortage trends for Products and Services across multiple regions 


![alt text](https://img.shields.io/github/languages/top/amruth21/shortage-trends-twitter "test") 
![alt text](https://img.shields.io/github/commit-activity/y/amruth21/shortage-trends-twitter "test")
![alt text](https://img.shields.io/github/stars/amruth21/shortage-trends-twitter?style=social "test")

## Description

The Shortage Trends bot utilizes the Tweepy PIP package to access various Twitter API endpoints. These endpoints were used in order to customize the Bot's profile and schedule posts with media/location. In order to fetch the shortage data, the bot uses an unofficial Google Trends API (pytrends) which queries for the most googled "shortages". This data was then used to generate graphs with MatPlotLib/Plotly that would visualize the data and help viewers contextualize the meaning behind it.  

## Theory

The Theory behind this Bot is that all the information is fetched from the Google Trends API. The Google Trends website lists the top queries related to a topic and their search popularity relative to each other. So the principle our bot operates on is that when a certain good is in shortage people will be more likely to search for term followed by shortage(ex: chip shortage). By applying this concept when pulling the google trends data for the search term "shortage" all the related top queries will be items that are in shortage. However it is important to cleanse the data for duplicates as well as things that could be searched alongside "shortage" that arent actual goods such as key terms like "is, are, how, 2022".  

![Alt text](static/trends.png?raw=true "Trends")


## Getting Started

### Dependencies

* Python3
* Tweepy
* pyTrends
* Conda
* Heroku
* MatPlotLib
* Pandas
* numpy
* dotenv

### Installing

```
git clone https://github.com/amruth21/shortage-trends-twitter
```

### Setting up Dependencies

When setting up the dependencies there are two different avenues that are provided. You can launch a Conda Virtual Environment if you have Conda installed or can pip install the packages.

#### Conda

```
conda env create -f environment.yml
conda activate twitterBot
conda env list
```
#### Pip

```
pip install -r requirements.txt
```

### Executing program

Twitter currently has two seperate API's with their own respective endpoints [APIv1](https://developer.twitter.com/en/docs/twitter-api/v1) and [APIv2](https://developer.twitter.com/en/support/twitter-api/v2). In order to accomodate for these API's there is two seperate bot files in the repository however keep in mind APIv2 has alot less capabailities for example you are unable to generate media IDs.

#### APIv1
Requires Elevated Access which you can apply for at [https://developer.twitter.com/en/portal/products]

#### APIv2
Requires Essential Access which is granted to everyone

#### Steps

* Activate your virutal enviroment if applicable

```
conda activate twitterBot
```
* Setting up bot on [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
    1. Enabling OAuth1.0 and Oauth2.0
    ![Alt text](static/auth.png?raw=true "Auth")
    2. Generate Auth Keys and Secrets (with read, write access)
    ![Alt text](static/keys.png?raw=true "Keys")
    3. Create .env file
    4. Configure environment variables(consumer_key, consumer_secret, access_token, access_token_secret, bearer_token)

Inside your Conda virtual environment to run locally
```
python src/scheduler.py
```

### Host on Heroku
To host on Heroku using the CLI follow these [instructions](https://medium.com/tech-insights/how-to-deploy-a-python-script-or-bot-to-heroku-in-5-minutes-a82de2d3ed40) or create an application on Heroku dashboard.

## Authors

Amruth Nare (amruthnare.1@gmail.com) completed on Aug 21, 2022

## MIT License
