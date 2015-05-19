#!/usr/bin/env python
import tweepy, time

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

accessFile = open("../accessDetails.txt", "rb")
CONSUMER_KEY = str(accessFile.readline()).rstrip()
CONSUMER_SECRET = str(accessFile.readline()).rstrip()
ACCESS_KEY = str(accessFile.readline()).rstrip()
ACCESS_SECRET = str(accessFile.readline()).rstrip()


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
results = api.search(q="obama", lang='EN')

for result in results:
    print result.text.encode('utf-8')