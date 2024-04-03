import math
from abc import ABC, abstractmethod
from functools import cached_property


class Shape2D(ABC):
    name: str = 'shape'

    def __init__(self, x: float = 0., y: float = 0.) -> None:
        self._x, self._y = x, y

    def __repr__(self) -> str:
        return f'<{self.name} at ({self._x}, {self._y})>'

    @abstractmethod
    def perimeter(self) -> float:
        ...

    @abstractmethod
    def area(self) -> float:
        ...


class Rectangle(Shape2D):
    name: str = 'rectangle'

    def __init__(self, width: float, height: float, x: float = 0., y: float = 0.) -> None:
        super().__init__(x, y)
        self._width, self._height = width, height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float) -> None:
        self._width = width

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height


class Square(Rectangle):
    name: str = 'square'

    def __init__(self, side: float, x: float = 0., y: float = 0.) -> None:
        super().__init__(side, side, x, y)

    def _set_width_height_simultaneously(self, v: float) -> None:
        Rectangle.height.fset(self, v)
        Rectangle.width.fset(self, v)

    @property
    def width(self) -> float:
        return super().width

    @property
    def height(self) -> float:
        return super().height

    @width.setter
    def width(self, width: float) -> None:
        self._set_width_height_simultaneously(width)

    @height.setter
    def height(self, height: float) -> None:
        self._set_width_height_simultaneously(height)

    def __repr__(self) -> str:
        assert self.width == self.height
        return f'<sqaure side={self.width}> at ({self._x}, {self._y})'


class Circle(Shape2D):
    name: str = 'circle'

    def __init__(self, radius: float, x: float = 0., y: float = 0.) -> None:
        super().__init__(x, y)
        self._radius = radius

    @cached_property
    def diameter(self) -> float:
        print('recalculated diameter.')
        return self._radius * 2

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self._radius = radius
        del self.diameter

    def area(self) -> float:
        return math.pi * math.pow(self._radius, 2)

    def perimeter(self) -> float:
        return math.pi * self.diameter

    def __repr__(self) -> str:
        return f'<circle r={self._radius} at ({self._x}, {self._y})>'


if __name__ == "__main__":
    square = Square(1.)
    print(f'Area of {square}: {square.area()}')
    square.width = 2.
    print(f'Area of {square}: {square.area()}')

    circle = Circle(1.)
    print(f'Diameter of {circle}: {circle.diameter}')
    print(f'Diameter of {circle}: {circle.diameter}')
    circle.radius = 2.
    print(f'Diameter of {circle}: {circle.diameter}')
