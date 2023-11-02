from time import sleep


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._diameter = None
        self._radius = value

    @property
    def diameter(self):
        if self._diameter is None:
            print('costly computation')
            self._diameter = self._radius * 2
        return self._diameter


a = Circle(3)
print(a.radius)
print(a.diameter)

a.radius = 4
print(a._diameter)
print('-')
print(a.diameter)
print(a.diameter ** 3)

from functools import cached_property


# this will not work as expected: will not update diameter when radius is changed
class CircleV2:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        print('costly computation')  # Simulate a costly computation
        return self.radius * 2
