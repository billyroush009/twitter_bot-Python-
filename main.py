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

##shows all the info pulled from the api
##dir(api)

##how to check api fields for the bots account
##me = api.me()
##me._json

##how to send a tweet through the API
##my_new_status = "From my desktop"
##new_status = api.update_status(my_new_status)

##declaring actual file name variable
FILE_NAME = 'last_seen.txt'

##these two methods check the "last_seen.txt" file to make sure duplicate responses arent' sent out every time the bot checks for new tweets
def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

##function that auto-replies when someone tweets "#testing" at the bot
def reply():
    ##calls the "read_last_seen" function to load up all the tweets posted since the id in the "last_seen.txt" file
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    ##pulls most recent tweets text content
    ##print(tweets[0].text)

    ##loops through all tweets where bot account in mentioned
    for tweet in reversed(tweets):
        ##checking if #testing was part of the tweets at the bot
        if '#hello' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            ##sending reply tweet to user
            api.update_status("Hey " + tweet.user.screen_name + " you're pretty great! @" + tweet.user.screen_name + " auto reply, like, and retweet!", tweet.id)
            ##favoriting the tweet sent at the bot
            api.create_favorite(tweet.id)
            ##retweeting the tweet sent at the bot
            api.retweet(tweet.id)
            ##updating text file w/ newest tweet id that has been replied to, stopping duplicate replies
            store_last_seen(FILE_NAME, tweet.id)

##loop keeping program alive and checking for messages to reply to every time.sleep(x), x = seconds
while True:
    reply()
    time.sleep(15)