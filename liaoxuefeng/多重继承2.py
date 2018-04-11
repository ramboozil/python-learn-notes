class A(object):
    def f(self):
        print('A')


class B(object):
    def f(self):
        print('B')


class C(B, A):
    pass


c = C()
c.f()


class A(object):
    def f(self):
        print('A')


class B(A):
    def f(self):
        print('AB')


class C(A):
    def f(self):
        print('CB')


class D(B, C):
    pass


d = D()
d.f()
print(D.__mro__)


