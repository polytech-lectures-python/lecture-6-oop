class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    total = 0
    length = 0

    def averager(new_value):
        nonlocal total
        total += new_value
        nonlocal length
        length += 1
        return total / length
    return averager


avg_oop = Averager()
print(avg_oop(1))
print(avg_oop(2))
print(avg_oop(3))


avg_fun = make_averager()
print(avg_fun(1))
print(avg_fun(2))
print(avg_fun(3))

print(avg_fun.__code__.co_varnames)
print(avg_fun.__code__.co_freevars)
