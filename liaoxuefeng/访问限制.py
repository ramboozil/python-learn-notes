class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get__name(self):
        return self.__name

    def get__gender(self):
        return self.__gender

    def set__name(self, name):
        self.__name = name

    def set__gender(self, gender):
        self.__gender = gender

    def print_info(self):
        print('%s %s' % (self.__name, self.__gender))


a = Student('diaoge', '女')
# print(a.__name) # __添加这个代表这个属性是私有的

a.__name = 'yangliucheng'
print(a.get__name())
print(a._Student__name)  # 内部已经将__name 重命名为_name

