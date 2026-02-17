class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def copy(self):
      return Point(self.x, self.y)
