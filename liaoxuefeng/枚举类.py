from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekeend(Enum):
    Sun = 1  # Sun的value被设定为0
    Mon = 2
    Tue = 3
    Wed = 4
    Thu = 5
    Fri = 6
    Sat = 7


print(Weekeend.Mon)
print(Weekeend['Sun']) # 通过成员的名称来获取成员
print(Weekeend(1))  # 通过成员的值来取枚举值

for m in Weekeend.__members__.items():
    print(m)


for name, member in Weekeend.__members__.items():
    print(name, '=>', member, ',', member.value)


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


s = Student('miaojie', Gender.Male)

print(Gender.Male)
print(type(()))
print(type(Enum))