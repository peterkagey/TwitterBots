from PIL import Image, ImageDraw
from botfons_needles.random_needle import RandomNeedle

class NeedleDrawer:
  def __init__(self):
    self.width   = 4096
    self.height  = 2048
    self.spacing = 256
    self.random_needles = self.toss_needles(100)

  def draw_vertical_lines(self):
    for x in range(self.spacing, self.width, self.spacing):
      self.drawing_context.line([(x,0),(x,self.height)],width=10, fill="black")

  def toss_needles(self, count):
    return [RandomNeedle(self.width, self.height, self.spacing) for _ in range(count)]

  def draw_needles(self):
    for needle in self.random_needles:
      needle.draw(self.drawing_context)

  def count_needles(self):
    cross_count = sum(1 for n in self.random_needles if n.crosses_line())
    return (cross_count, len(self.random_needles))

  def draw_image(self):
    img = Image.new("RGB", (self.width, self.height), (255,255,255))
    self.drawing_context = ImageDraw.Draw(img)
    self.draw_needles()
    self.draw_vertical_lines()
    del self.drawing_context
    file_name = "/tmp/needle_drop.png"
    img.save(file_name)
    return file_name
