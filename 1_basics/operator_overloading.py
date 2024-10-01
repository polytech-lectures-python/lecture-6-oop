def CyclicGroup(n):
    class CyclicGroupN:
        def __init__(self, m):
            self.__n = n
            self.m = m % self.__n

        def __add__(self, other):
            return (self.m + other.m) % self.__n

    return CyclicGroupN


CyclicGroup3 = CyclicGroup(3)

print(CyclicGroup3(10) + CyclicGroup3(11))
