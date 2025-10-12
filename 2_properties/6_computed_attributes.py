import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return math.dist((0, 0), (self.x, self.y))

    @property
    def angle(self):
        return math.degrees(math.atan(self.y / self.x))

    def as_cartesian(self):
        return self.x, self.y

    def as_polar(self):
        return self.distance, self.angle


point = Point(4, 3)
print(point.x, point.y)

print(point.distance)

print(point.angle)

print(point.as_cartesian())

print(point.as_polar())
