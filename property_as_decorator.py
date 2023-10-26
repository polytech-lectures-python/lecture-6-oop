class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        if value >= 0:
            self._radius = value
        else:
            raise ValueError(f"Invalid value in radius.setter: {value}. "
                             f"Should be non-negative")

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius


circle = Circle(3.0)
print(circle.radius)

circle.radius = 4.0
print(circle.radius)

# del circle.radius
# print(circle.radius)
