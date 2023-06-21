from tweeter import Tweeter
from oeis_triangles.secrets import *
from oeis_triangles.json_accountant import JSONAccountant
from oeis_triangles.oeis_drawer import OEISDrawer
# from oeis_triangles.triangle_grower import TriangleGrower

class OEISTriangles(Tweeter):
  def __init__(self):
    super().__init__(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN)

  def tweet(self, a_number=None, tweet_copy=None):
    if (a_number == None) | (tweet_copy == None):
      accountant = JSONAccountant() # Get a new one each time, just in case.
      (a_number, tweet_copy) = accountant.get_todays_sequence()
    OEISDrawer(a_number).draw()
    file_with_path = "/tmp/" + a_number + ".png"
    media = self.api.media_upload(filename=file_with_path)
    self.client.create_tweet(text=tweet_copy, media_ids=[media.media_id_string])
