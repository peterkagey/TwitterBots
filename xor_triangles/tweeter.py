from tweeter import Tweeter
from xor_triangles.secrets import *
from xor_triangles.triangle_drawer import TriangleDrawer
from xor_triangles.seed_maker import SeedMaker
from xor_triangles.triangle_grower import TriangleGrower

class XorTriangles(Tweeter):
  def __init__(self, modulus):
    super().__init__(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN)
    self.modulus = modulus

  def tweet(self, seed=None, tweet_copy=None):
    if not seed:
      (seed, tweet_copy) = SeedMaker(self.modulus).get_todays_basis_vector()
    triangle = TriangleGrower(self.modulus).make_triangle(seed)
    filename = TriangleDrawer(triangle).draw_triangular_image()
    media = self.api.media_upload(filename=filename)
    self.client.create_tweet(text=tweet_copy, media_ids=[media.media_id_string])
