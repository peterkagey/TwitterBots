import sys
sys.path.append('/Users/peter/Programming/bot_central/')
from botzier_curves.tweeter import BotzierCurvesTweeter
from robot_walks.robot_walks_tweeter import RobotWalksTweeter
from xor_triangles.tweeter import XorTrianglesTweeter

def handler(event, _):
  if not "account_name" in event:
    raise Error("Which account??")
  else:
    match event["account_name"]:
      # case "@BotfonsNeedles":
      #   bot = "BotfonsNeedles"
      #   # Look up last tweet.
      #   # Feed data to bot
      case "@BotzierCurves":
        account = BotzierCurvesTweeter()
        account.tweet()
      # case "@oeisTriangles":
      #   account = "oeisTriangles"
      case "@RobotWalks":
        # TODO: read step_size and step_pattern from event.
        account = RobotWalksTweeter()
        account.tweet(step_size=None, step_pattern=None)
      case "@xorTriangles":
        account = XorTrianglesTweeter(modulus=3)
        account.tweet()

handler({"account_name": "@xorTriangles"}, 1)