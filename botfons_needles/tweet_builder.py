from botfons_needles.needle_drawer import NeedleDrawer
from math import pi
import re

class TweetBuilder:

    def __init__(self, last_tweet_copy):
      self.drawer   = NeedleDrawer()
      self.last_tweet_copy = last_tweet_copy

    # Reports the all digits of the estimate which agree with pi, plus two more.
    def pi_digits_difference(self, estimate):
      characters = 4
      estimate_string = str(estimate)
      pi_string = "3.1415926535897932384626433832795028841971"
      while estimate_string[:(characters - 1)] == pi_string[:(characters - 1)]:
        characters += 1
      return estimate_string[:characters]

    # Writes the error as a percentage with three significant digits.
    def error_estimate(self, estimate):
      def significant_digits(x):
        if x == 0:
          return "0"
        n = 0
        while x * 10**n < 1 and x * 10**n > - 1:
          n += 1
        return ("%." + str(n) + "f") % (x * 100) + "%"
      error = (estimate - pi)/pi
      return "an error of " + significant_digits(error)

    # Reads the previous tweet, and updates it with the current trial.
    def get_running_estimate(self, trial_crossed, trial_dropped):
      running_estimate_regex = re.compile('(\d+) of (\d+)')
      matches = running_estimate_regex.findall(self.last_tweet_copy)
      if len(matches) == 1:
        (crossed, total) = matches[0]
        return (int(crossed) + trial_crossed, int(total) + trial_dropped)
      else:
        return (trial_crossed, trial_dropped)

    # Composes the words to tweet.
    def tweet_copy(self):
      (current_crossed, current_total) = self.drawer.count_needles()
      trial_estimate = 2*(current_total/current_crossed)
      trial_drop = 'This trial dropped {} needles, {} of which crossed a line. '.format(current_total, current_crossed)
      trial_pi = 'This estimates π ≈ 2*({}/{}) ≈ {}, {}.'.format(current_total, current_crossed, self.pi_digits_difference(trial_estimate), self.error_estimate(trial_estimate))

      (previous_crossed, previous_total) = self.get_running_estimate(current_crossed, current_total)
      total_estimate = 2*(previous_total/previous_crossed)
      total_drop = 'In total, {} of {} needles have crossed a line.'.format(previous_crossed, previous_total)
      total_pi = "This estimates π ≈ {}, {}.".format(self.pi_digits_difference(total_estimate), self.error_estimate(total_estimate))
      return trial_drop + trial_pi + "\n\n" + total_drop + "\n" + total_pi

    def build_tweet(self):
      file_name = self.drawer.draw_image()
      copy = self.tweet_copy()
      return (file_name, copy)
