class Animal(object):
    def run(self):
        print('animnal is runnning')


class Dog(Animal):
    def run(self):
        print('dog is running')
        

class Cat(Animal):
    def run(self):
        print('cat is running')


class Diaoge(object):
    def run(self):
        print('Diaoge is running slowly')


def run(animal):
    animal.run()
    animal.run()


a = Cat()
b = Dog()
c = Diaoge()

a.run()
b.run()
c.run()

print(isinstance(a, Animal))
print(isinstance(b, Animal))
print(isinstance(c, Animal))