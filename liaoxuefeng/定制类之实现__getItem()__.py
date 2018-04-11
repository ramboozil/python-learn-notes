class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for i in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print(dir(Fib))