import os
import json
import tweepy 
import time

is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
    #here goes all your heroku config
    consumer_key = os.environ.get('twitter_consumer_key', None)
    consumer_secret = os.environ.get('twitter_consumer_secret', None)
    access_token = os.environ.get('twitter_access_token', None)
    access_token_secret = os.environ.get('twitter_access_token_secret', None)
    print('production')
else:
    print('development')
    api_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath('__file__')))))
    file_name = os.path.join(api_dir, "api_keys.json")
    data = json.load(open(file_name))
    consumer_key = data['twitter_consumer_key']
    consumer_secret = data['twitter_consumer_secret']
    access_token = data['twitter_access_token']
    access_token_secret = data['twitter_access_token_secret']


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())



# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Live, from Heroku! Can't stop. Won't stop. This is Tweet #%s!" %
        tweet_number)

counter = 0
for x in range(3):
# Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1