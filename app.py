import sys
sys.path.append('/Users/peter/Programming/bot_central/')
from botzier_curves.tweeter import BotzierCurves
from robot_walks.tweeter import RobotWalks
from xor_triangles.tweeter import XorTriangles
from oeis_triangles.tweeter import OEISTriangles

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
        account = BotzierCurves()
        account.tweet()
      case "@oeisTriangles":
        account = OEISTriangles()
        account.tweet()
      case "@RobotWalks":
        # TODO: read step_size and step_pattern from event.
        account = RobotWalks()
        account.tweet(step_size=None, step_pattern=None)
      case "@xorTriangles":
        account = XorTriangles(modulus=3)
        account.tweet()

handler({"account_name": "@oeisTriangles"}, 1)