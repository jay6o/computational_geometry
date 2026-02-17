from point import Point
import random

class Generator:
  """
    Generates n points in the 2D plane
  """
  def generate(self, n):
    points = []
    for _ in range(0, n):
      x = random.uniform(-1000000,1000000)
      y = random.uniform(-1000000,1000000)
      points.append(Point(x, y))
    return points
