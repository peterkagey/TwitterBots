from tweeter import Tweeter
from botzier_curves.secrets import *
from botzier_curves.curve_drawer import BezierCurveDrawer
from botzier_curves.caption_maker import CaptionMaker

class BotzierCurves(Tweeter):
  def __init__(self):
    super().__init__(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN)

  def tweet(self):
    image_filename = BezierCurveDrawer().draw_it()
    caption = CaptionMaker().caption()
    media = self.api.media_upload(filename=image_filename)
    self.client.create_tweet(text=caption, media_ids=[media.media_id_string])
