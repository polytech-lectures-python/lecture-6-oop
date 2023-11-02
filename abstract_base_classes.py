from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def n_sides(self):
        pass


class Triangle(Polygon):

    def n_sides(self):
        return 3


class Rectangle(Polygon):

    # overriding abstract method
    def n_sides(self):
        return 4


class Hexagon(Polygon):

    def n_sides(self):
        return 6


polygones = [Triangle(), Rectangle(), Rectangle(), Hexagon()]

for x in polygones:
    print(f"{x}: {x.n_sides()}")
