class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @classmethod
    def from_length(cls, start, length):
        return cls(start, start + length)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


i1 = Interval(1, 3)
i2 = Interval.from_length(1, 2)
print(i1 == i2)
