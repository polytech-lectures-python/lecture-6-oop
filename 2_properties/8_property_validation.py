class PointInitValidationError(ValueError):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def validate(value):
        try:
            result = float(value)
            print("Validated!")
            return result
        except ValueError:
            raise PointInitValidationError('Input must be a number')


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
        self._y = self.validate(value)

