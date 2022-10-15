from oeis_triangles.b_file_parser import BFileParser
from oeis_triangles.b_file_lookup import BFileLookup
from oeis_triangles.sequence_drawer import SequenceDrawer

class OEISDrawer:
  def __init__(self, a_number):
    self.sequence_name = a_number
    b_file = BFileLookup(a_number).b_file_txt()
    data = BFileParser(b_file).parsed_data
    self.sequence = list(map(lambda t: t[1], data))

  def draw(self):
    SequenceDrawer(self.sequence, self.sequence_name).draw()
