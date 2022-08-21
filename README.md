# shortage-trends-twitter
A twitter bot programmed using Python3 to fetch and post Shortage trends for Products and Services across multiple regions 


![alt text](https://img.shields.io/github/languages/top/amruth21/shortage-trends-twitter "test") 
![alt text](https://img.shields.io/github/commit-activity/y/amruth21/shortage-trends-twitter "test")
![alt text](https://img.shields.io/github/stars/amruth21/shortage-trends-twitter?style=social "test")

## Description

The Shortage Trends bot utilizes the Tweepy PIP package to use various Twitter API endpoints. These endpoints were used in order to customize the Bot's profile and schedule posts with media/location. In order to fetch the shortage data, the bot uses an unofficial Google Trends API (pytrends) which queries for the most googled "shortages". This data was then used to generate graphs with MatPlotLib/Plotly that would visualize the data and help viewers contextualize the meaning behind it.  

## Theory

The bot derives its information from the principle that what people tend to search for as shortages such as "chip shortage" tends to be the good/service that is actually in shortage. By applying this principle and pulling google trends data for the search term "shortage" after cleansing I was able to grab a list of the top 10 terms that were googled with shortage(ex: food shortage, formula shortage).
ADD IMAGE OF GOOGLE TRENDS WEBSITE

## Getting Started

### Dependencies

* Python3
* Tweepy
* Heroku
* MatPlotLib
* dotenv
* Pandas
* pyTrends
* numpy

### Installing

```
git clone https://github.com/amruth21/shortage-trends-twitter
```

### Executing program

Twitter currently has two seperate API's with their own respective endpoints [APIv1](https://developer.twitter.com/en/docs/twitter-api/v1) and [APIv2](https://developer.twitter.com/en/support/twitter-api/v2). In order to accomodate for these API's there is two seperate bot files in the repository however keep in mind APIv2 has alot less capabailities for example you are unable to generate media IDs.

#### APIv1
Requires Elevated Access which you can apply for at [https://developer.twitter.com/en/portal/products]

#### APIv2

* Locally running the bot

```
python3 src install
```
```
npm run start
```
* Setting up remote hosting
    1. Create a Heroku application
    2. Set buildpack to Nodejs
    3. Configure environment variables(BOT_TOKEN, USERID, Basic_AUTH)
    4. Set up automatic deploys from GitHub main branch repository  

## Authors

Amruth Nare (amruthnare.1@gmail.com)

## MIT License
