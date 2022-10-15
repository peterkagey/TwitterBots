from tweeter import Tweeter
from xor_triangles.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from xor_triangles.triangle_drawer import TriangleDrawer
from xor_triangles.seed_maker import SeedMaker
from xor_triangles.triangle_grower import TriangleGrower

class XorTriangles(Tweeter):
  def __init__(self, modulus):
    super().__init__(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    self.modulus = modulus
  
  def tweet(self, seed=None, tweet_copy=None):
    if not seed:
      (seed, tweet_copy) = SeedMaker(self.modulus).get_todays_basis_vector()
    triangle = TriangleGrower(self.modulus).make_triangle(seed)
    filename = TriangleDrawer(triangle).draw_triangular_image()
    self.api.update_status_with_media(filename=filename, status=tweet_copy)
