from types import MethodType


class Student(object):
    pass


def set__score(self, score):
    self.score = score


s = Student()

# Student.set__score = set__score
Student.set__score = MethodType(set__score, Student)

# s.set__score = set__score
# s.set__score = MethodType(set__score, s)

# s.set__score(self=s, score=100)
# s.set__score(100)
# print(s.score)

s2 = Student()
# s2.set__score()  实例绑定方法 只对当前实例生效
s2.set__score(100)  # MethodType绑定方法或者属性到类 并不是真的将其写入方法的内部 具体详见笔记    s2内部并没有这个属性
print(dir(Student))