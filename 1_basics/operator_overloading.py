def cyclic_group_factory(n):
    class CyclicGroupN:
        def __init__(self, m):
            self.__n = n
            self.m = m % self.__n

        def __add__(self, other):
            return (self.m + other.m) % self.__n

    return CyclicGroupN


CyclicGroup3 = cyclic_group_factory(3)

print(CyclicGroup3(10) + CyclicGroup3(11))
