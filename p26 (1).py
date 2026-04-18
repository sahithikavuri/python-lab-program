import math

class Shape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

s = Shape(5)
print("Area:", s.area())
