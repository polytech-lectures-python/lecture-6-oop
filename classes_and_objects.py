class A:
    i = 123

    def f(self):
        return 'f'



class B:
    x = 123

    def __init__(self, b):
        self.c = b

    def f(self):
        return B.x + self.c


a = A()
print(a.f())
print(A.f(a))
# print(a.g)
# print(A.g)
# print(A.g())
# print(a.g())
