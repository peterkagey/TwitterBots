from tweeter import Tweeter
from botzier_curves.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY,API_KEY_SECRET
from botzier_curves.curve_drawer import BezierCurveDrawer
from botzier_curves.caption_maker import CaptionMaker

class BotzierCurvesTweeter(Tweeter):
    def __init__(self):
        super().__init__(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def tweet(self):
        image_filename = BezierCurveDrawer().draw_it()
        caption = CaptionMaker().caption()
        self.api.update_status_with_media(filename=image_filename, status=caption)