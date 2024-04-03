class A:
    i = 123

    def f(self):
        return 'f'


class B(A):
    x = 123

    def __init__(self, b):
        self.__c = b

    def __repr__(self):
        return f"B({self.__c})"

    def f(self):
        return B.x + self.c


a = A()
print(a.f())
print(A.f(a))
# print(a.g)
# print(A.g)
# print(A.g())
# print(a.g())
