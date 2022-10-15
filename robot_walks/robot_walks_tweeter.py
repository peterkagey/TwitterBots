from tweeter import Tweeter
from robot_walks.secrets import *
from robot_walks.robot_walk_drawer import RobotWalkDrawer

class RobotWalksTweeter(Tweeter):
    def __init__(self):
        super().__init__(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

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
        drawer         = RobotWalkDrawer(step_size, step_pattern)
        image_filename = drawer.draw_image()
        step_size      = "Step size: 1/" + str(drawer.step_size) + "."
        step_pattern   = "Step pattern: " + self.pattern_word(drawer.seed) + "."
        caption        = step_size + "\n" + step_pattern
        self.api.update_status_with_media(filename=image_filename, status=caption)