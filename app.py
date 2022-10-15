import sys
sys.path.append('/Users/peter/Programming/bot_central/')
from botzier_curves.tweeter import BotzierCurves
from robot_walks.tweeter import RobotWalks
from xor_triangles.tweeter import XorTriangles
from oeis_triangles.tweeter import OEISTriangles
from botfons_needles.tweeter import BotfonsNeedles

def handler(event, _):
  if not "account_name" in event:
    raise ValueError("No 'account_name' specified.")
  else:
    if event['account_name'] == "@BotfonsNeedles":
      account = BotfonsNeedles()
      account.tweet()
    elif event['account_name'] == "@BotzierCurves":
      account = BotzierCurves()
      account.tweet()
    elif event['account_name'] == "@oeisTriangles":
      a_number = event.get('a_number', None)
      tweet_copy = event.get('tweet_copy', None)
      account = OEISTriangles()
      account.tweet(a_number, tweet_copy)
    elif event['account_name'] == "@RobotWalks":
      step_size = event.get('step_size', None)
      step_pattern = event.get('step_pattern', None)
      account = RobotWalks()
      account.tweet(step_size, step_pattern)
    elif event['account_name'] == "@xorTriangles":
      modulus = event.get('modulus', 2)
      seed = event.get('seed', None)
      tweet_copy = event.get('tweet_copy', None)
      account = XorTriangles(modulus)
      account.tweet(seed, tweet_copy)
    else:
      raise ValueError("Unknown 'account_name' supplied.")
  return "Successfully posted to " + event['account_name'] + "! :)"
