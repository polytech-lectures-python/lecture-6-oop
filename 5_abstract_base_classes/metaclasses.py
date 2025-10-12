class ExclusiveFooBarMeta(type):
    def __new__(cls, name, bases, attrs):
        if 'foo' in attrs and 'bar' in attrs:
            raise TypeError(f'Class {name} cannot contain both foo and bar attributes.')
        if 'foo' not in attrs and 'bar' not in attrs:
            raise TypeError(f'Class {name} must provide either a foo attribute or a bar attribute.')
        else:
            print('Success')

        return super(ExclusiveFooBarMeta, cls).__new__(cls, name, bases, attrs)


# class FooBar(metaclass=ExclusiveFooBarMeta):
#     foo = 'foo'
#     bar = 'bar'


class Foo(metaclass=ExclusiveFooBarMeta):
    foo = 1


class Bar(metaclass=ExclusiveFooBarMeta):
    bar = 'bar'


class Neither(metaclass=ExclusiveFooBarMeta):
    pass
