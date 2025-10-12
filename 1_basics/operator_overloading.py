def cyclic_group_factory(n):
    class CyclicGroupN:
        base = n
        def __init__(self, m):
            self.m = m % self.base

        def __add__(self, other):
            return (self.m + other.m) % self.base

    return CyclicGroupN


CyclicGroup3 = cyclic_group_factory(3)

print(CyclicGroup3(10) + CyclicGroup3(11))
