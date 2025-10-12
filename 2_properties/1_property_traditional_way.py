import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def _set_diameter(self, d):
        self.radius = d / 2

    diameter = property(fget=lambda self: 2 * self.radius,
                        fset=_set_diameter)

    area = property(fget=lambda self: math.pi * self.radius**2)


circle = Circle(3.0)
print(circle.radius)

circle.radius = 4.0
print(circle.radius)
