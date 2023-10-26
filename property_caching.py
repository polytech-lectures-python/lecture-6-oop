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
            sleep(1)  # costly computation
            self._diameter = self._radius * 2
        return self._diameter


from functools import cached_property


class CircleV2:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def diameter(self):
        sleep(0.5)  # Simulate a costly computation
        return self.radius * 2
