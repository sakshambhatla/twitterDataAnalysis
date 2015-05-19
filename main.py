#!/usr/bin/env python
import tweepy, time

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

accessFile = open("../accessDetails.txt", "rb")
CONSUMER_KEY = str(accessFile.readline()).rstrip()
CONSUMER_SECRET = str(accessFile.readline()).rstrip()
ACCESS_KEY = str(accessFile.readline()).rstrip()
ACCESS_SECRET = str(accessFile.readline()).rstrip()

lastID=0

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print api.rate_limit_status()


while True:
	results = api.search(q="testbot sbhatla", since_id = lastID)
	try:
		lastID = results[0].id
	except:
		pass
	#print lastID
	for result in results:
		print result.id, result.author.name, result.favorite_count, result.retweet_count
		#print result.favorite_count
		#print result.author.name
		#print result.author.screen_name
		#print result.author.followers_count
		#print result.retweet_count
		print result.text.encode('utf-8')

	time.sleep(3)
	