#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import json
import os

# Parameter should be formatted with @mention or #mention. Multiple parameters should be split with commas
def pull(mention):
    # Twitter API credentials
    credentialsPath = r'credentials'
    with open(os.path.join(credentialsPath, 'twitter_credentials.json')) as cred_data:
        info = json.load(cred_data)
        consumer_key = info['CONSUMER_KEY']
        consumer_secret = info['CONSUMER_SECRET']
        access_key = info['ACCESS_KEY']
        access_secret = info['ACCESS_SECRET']

    # Create the api endpoint

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)

    # paramaters to search for
    parameters = mention.replace(", ", " OR ")

    results = []

    for tweet_info in tweepy.Cursor(api.search, q=parameters,
                            tweet_mode='extended'):
        results.append(tweet_info)
    
    print ('Extracted ' + str(len(results)) 
        + ' tweets with ' + mention)
    
    return results