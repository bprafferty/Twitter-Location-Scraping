"""
Author: Brian Rafferty
Project: Twitter Location Scraping
Date: 9/4/19
"""
import json
import csv
import tweepy
import re

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes 
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API, wait_on_rate_limit prevents crossing rate thresholds
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % (fname), 'wb') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count', 'longitude', 'latitude'])
        
        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(1000000):
            
            #determine if geo_location is active, and record only if online
            if (tweet.coordinates is not None):
                point = tweet.coordinates
                print(point)
                w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count, point['coordinates'][0], point['coordinates'][1]])
                
            
consumer_key = raw_input('Enter Consumer Key: ')
consumer_secret = raw_input('Enter Consumer Secret:')
access_token = raw_input('Enter Access Token:')
access_token_secret = raw_input('Enter Access Secret:')
    
hashtag_phrase = raw_input('Hashtag Phrase: ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)