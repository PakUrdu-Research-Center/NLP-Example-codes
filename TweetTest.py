import tweepy

# Enter your API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connect to the API
api = tweepy.API(auth)

# Search for tweets on a given topic
query = "nlp"
tweets = api.search(q=query, count=100, tweet_mode='extended')

# Print the text of the latest tweets
for tweet in tweets:
    print(tweet.full_text)
