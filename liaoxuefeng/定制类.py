class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print()
# print(Chain().users('michael').repos)


# '/status/user/timeline/list'


class Chain():
    def __init__(self, path=''):
        print('init', path)
        self.path = path

    def __getattr__(self, path):
        print('getattr')
        return Chain('%s/%s' % (self.path, path))

    def __call__(self, path):
        print('call')
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__


print(Chain().a.b("ChenTian").c.d)
