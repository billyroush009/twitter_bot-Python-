import tweepy
import time

##setting API and token value variables, provided from Twitter
consumer_key = "pRGjE5nAdzf7PkWGpXvVItzl5"
consumer_secret = "DzjRKpxiix7MHq9RL5WQqvjPJBN0OLA75oHEB7tx85N54Y3JgX"
access_token = "1392187002594988037-j1UcadYrp2KaF5gCW1avKAiUfbsAd3"
access_token_secret = "BWSfGd1cNWLFr9mGxVFFBqcWjoO61ev6SAKkj8CTTMBap"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

##the hashtag being searched for
hashtag = "#abcd1234"
##how many tweets will be responded to
tweetNumber = 10

##populating variable w/ "tweetNumber" amount of tweets that contain the "hashtag"
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

##function to retweet the found tweets
def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(2)
        ##error catch in case something goes wrong
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)
##initializing the actual search
searchBot()