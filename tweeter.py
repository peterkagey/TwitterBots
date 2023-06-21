import tweepy

# Everything that connects to the account should go here.
class Tweeter:
  def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, bearer_token=None):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.api = tweepy.API(auth)
    self.client = tweepy.Client(
      bearer_token=bearer_token,
      consumer_key=consumer_key,
      consumer_secret=consumer_secret,
      access_token=access_token,
      access_token_secret=access_token_secret
    )

def tweet(self):
    NotImplementedError("TwitterConnection.tweet has not been implemented")
