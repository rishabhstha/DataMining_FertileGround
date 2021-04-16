from datetime import datetime
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time

consumer_key = "P5i8oS0DWMlplkEPWHewdcvnZ"
consumer_secret = "opXG0LpwkrMCPjogMdTikFXWbbvI2tnKFglG1YOc1BQj04Uvan"
access_token = "4091794879-nfBkiutGX2qkiVbETwsxOXENrk4ALrqV8keqSG4"
access_token_secret = "bZDq7LGETyqILIogC4IOSDMkaQKjYdc3wSEBJ3r2NgZsJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

username = '_fertileground_'
count = 1000

username = input("Enter the username of the twitter account:")
count = int(input("Enter the maximum number of tweets you want to access:"))


try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.user_timeline, id=username,
                           tweet_mode='extended').items(count)

    # Pulling information from tweets iterable object
    tweets_list = [[tweet.created_at, tweet.id, tweet.full_text, tweet.user.location]
                   for tweet in tweets]

    # Creation of dataframe from tweets list
    # Add or remove columns as you remove tweet information
    tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
    print('failed on_status,', str(e))
    time.sleep(3)

tweets_df.columns = ['Tweet Date', 'Tweet ID', 'Tweet text', 'Tweet Location']
print(tweets_df)
# tweets_df.to_csv('fertilegroundtweets.csv')
