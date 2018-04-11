class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Student Object: %s %s' % (self.name, self.age)

    __repr__ = __str__


Student('miaojie', 18)
