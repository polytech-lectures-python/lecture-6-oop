class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def validate(self, value):
        try:
            result = float(value)
            print("Validated x!")
            return result
        except ValueError:
            raise ValueError('"x" must be a number') from None


    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = self.validate(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated y!")
        except ValueError:
            raise ValueError('"y" must be a number') from None
