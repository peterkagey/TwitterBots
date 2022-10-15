from tweeter import Tweeter
from botfons_needles.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET_KEY
from botfons_needles.tweet_builder import TweetBuilder

class BotfonsNeedles(Tweeter):
  def __init__(self):
    super().__init__(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  
  def read_last_tweet(self):
    timeline = self.api.user_timeline(count=1, exclude_replies=True, tweet_mode='extended')
    return timeline[0].full_text

  def tweet(self):
    (file_name, copy) = TweetBuilder(self.read_last_tweet()).build_tweet()
    self.api.update_status_with_media(filename=file_name, status=copy)