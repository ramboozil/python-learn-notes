import types

print(type(123) == type(456))
print(type(abs) == type(str))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x, y: y + x) == types.LambdaType)

print(isinstance(123, int))
print(isinstance('a', str))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (tuple, list)))

print(dir(1))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


o = MyObject()
print(hasattr(o,'x'))
print(o.x)
print(getattr(o, 'x'))
# print(getattr(o, 'z'))
print(setattr(o, 'z', '404'))
print(getattr(o, 'z'))
print(getattr(o, 'y', 404))

print(getattr(o, 'power'))

f = getattr(o, 'power')
print(f)
print(f())