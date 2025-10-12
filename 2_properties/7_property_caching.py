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
            sleep(5)
            self._diameter = self._radius * 2
        return self._diameter


# a = Circle(3)
# print(a.radius)
# print(a.diameter)
#
# a.radius = 4
# print(a._diameter)
# print('-')
# print(a.diameter)
# print(a.diameter ** 3)

from functools import cache, cached_property, lru_cache


class CircleV2:
    def __init__(self, radius):
        self.radius = radius

    @lru_cache(maxsize=100)
    def __f(self, r):
        print('costly computation')  # Simulate a costly computation
        sleep(3)
        return r * 2

    # @cached_property
    @property
    def diameter(self):
        return self.__f(self.radius)
        # print('costly computation')  # Simulate a costly computation
        # return 2 * self.radius
