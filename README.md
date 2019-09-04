Author: Brian Rafferty
Project: Twitter Location Scraping
Date: 9/4/19
Details: This file allows the user to search for a hashtags on Twitter
and collects only those with geo_location data available. All data will
be printed into a CSV file, which can be used for future mapping.
To run: 
1. Sign up as Twitter Developer and write down API keys
2. Install tweepy library
3. Run code with: python tweetLocationScraper.py
4. Enter your 4 Twitter Developer API keys
5. Enter your hashtag phrase:
    Ex 1: #Hello
    Ex 2: #Hello AND #World
    Ex 3: #Hello OR #World