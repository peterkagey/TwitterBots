from tweeter import Tweeter
from robot_walks.secrets import *
from robot_walks.robot_walk_drawer import RobotWalkDrawer

class RobotWalks(Tweeter):
  def __init__(self):
    super().__init__(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN)

  def pattern_word(self,seed):
    step_value = seed
    walk_pattern = []
    while step_value > 0:
      if step_value & 1 == 1:
        walk_pattern.insert(0, "R")
      else:
        walk_pattern.insert(0, "L")
      step_value >>= 1
    return "".join(walk_pattern)

  def tweet(self, step_size=None, step_pattern=None):
    drawer     = RobotWalkDrawer(step_size, step_pattern)
    image_filename = drawer.draw_image()
    step_size    = "Step size: 1/" + str(drawer.step_size) + "."
    step_pattern   = "Step pattern: " + self.pattern_word(drawer.seed) + "."
    caption    = step_size + "\n" + step_pattern
    media = self.api.media_upload(filename=image_filename)
    self.client.create_tweet(text=caption, media_ids=[media.media_id_string])
