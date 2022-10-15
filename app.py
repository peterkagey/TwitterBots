import sys
sys.path.append('/Users/peter/Programming/bot_central/')
from botzier_curves.tweeter import BotzierCurves
from robot_walks.tweeter import RobotWalks
from xor_triangles.tweeter import XorTriangles
from oeis_triangles.tweeter import OEISTriangles
from botfons_needles.tweeter import BotfonsNeedles

def handler(event, _):
  if not "account_name" in event:
    raise Error("Which account??")
  else:
    match event["account_name"]:
      case "@BotfonsNeedles":
        account = BotfonsNeedles()
        account.tweet()
      case "@BotzierCurves":
        account = BotzierCurves()
        account.tweet()
      case "@oeisTriangles":
        # TODO: allow user to specify a_number and tweet_copy
        account = OEISTriangles()
        account.tweet(a_number=None, tweet_copy=None)
      case "@RobotWalks":
        # TODO: read step_size and step_pattern from event.
        account = RobotWalks()
        account.tweet(step_size=None, step_pattern=None)
      case "@xorTriangles":
        # TODO: allow user to specify seed and tweet_copy
        account = XorTriangles(modulus=3)
        account.tweet(seed=None, tweet_copy=None)
