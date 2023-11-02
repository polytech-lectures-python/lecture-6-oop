class A:
    def f(self, x):
        print(f"Running f({self}, {x})")

    @classmethod
    def class_f(cls, x):
        print(f"Running class_f({cls}, {x})")

    @staticmethod
    def static_f(x):
        print(f"Running static_f({x})")


a = A()

a.f(1)

a.class_f(1)
A.class_f(1)

a.static_f(1)
a.static_f(1)
