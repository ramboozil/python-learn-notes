import sys
from functools import reduce

class TestA:
    attr = 1

    def __init__(self, attr):
        self.attr = attr


obj_a = TestA(42)
print(TestA.__dict__)

obj1 = 1
obj2 = 'String!'
obj3 = []
obj4 = {}
print(type(obj1), type(obj2), type(obj3), type(obj4))


print(sys.path[3])

s = '0123456789'
result = reduce(lambda x, y: y+x, s)
print(s[1:7:6])