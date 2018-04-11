from functools import reduce


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


prod([3, 5, 7, 9])


def prod2(L):
    return reduce(lambda x, y: x * y, L)


# 将'123.456'转换成浮点数123.456
# 思路1：根据.号切成两部分求和
# 2 直接转换成整数*小数的十次幂
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }
    length = len(s.split('.')[1])
    print(s)
    # return reduce(lambda x, y: x * 10 + y, [i for i in map(lambda x: DIGITS[x], s) if isinstance(i, int)]) / 10 ** length
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], [i for i in s if i != '.'])) / 10 ** length


str2float('123.456')
(4*10+5 )*10