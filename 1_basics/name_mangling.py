class DemoClass:
    def __init__(self):
        self.__superprivate = 'superprivate'
        self._semiprivate = 'semiprivate'


class A(DemoClass):
    def f(self):
        print(self._semiprivate)


c = DemoClass()
b = A()

# print(c.__superprivate)

print(c._DemoClass__superprivate)
print(c._semiprivate)
print(c.__dict__)

print(b._DemoClass__superprivate)
print(b._semiprivate)
print(b.__dict__)