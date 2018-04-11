def lazy_sum(*args):
    total = 0
    for i in args:
        total = total + i
        return total


# print(lazy_sum(1, 3, 4, 5))


def lazy_sum2(*args):
    def sum():
        total = 0
        for i in args:
            total = total + i
        return total

    return sum


f = lazy_sum2(1, 3, 5, 6, 7)
print(f())