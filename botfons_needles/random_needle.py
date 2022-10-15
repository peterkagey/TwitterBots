import math
import random

class RandomNeedle:
  def __init__(self, canvas_width, canvas_height, line_spacing):
    theta = random.random()*math.pi
    half_needle = line_spacing//2
    self.x = random.randint(half_needle, canvas_width-half_needle)
    self.y = random.randint(half_needle, canvas_height-half_needle)
    self.del_x = half_needle * math.cos(theta)
    self.del_y = half_needle * math.sin(theta)
    self.spacing = line_spacing

  def crosses_line(self):
    initial_sector = (self.x - self.del_x)//self.spacing
    terminal_sector = (self.x + self.del_x)//self.spacing
    return initial_sector != terminal_sector

  def draw(self, drawing_context):
    color = "red" if self.crosses_line() else "grey"
    initial_point  = (self.x-self.del_x, self.y-self.del_y)
    terminal_point = (self.x+self.del_x, self.y+self.del_y)
    drawing_context.line([initial_point, terminal_point], "white", 16)
    drawing_context.line([initial_point, terminal_point], color, 8)
