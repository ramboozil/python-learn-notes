# 求从3开始的奇数
def _odd_num():
    n = 1
    while True:
        n = n + 2
        yield n


# 测试
def test(max):
    for i in _odd_num():
        if i < max:
            print(i)


# 去除3，5，7等奇数的倍数
def _not_divisiable(n):
    return lambda x: x % n > 0  # 相当于返回了一个函数对象


def primes():
    n = 2
    yield n
    it = _odd_num()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n), it)


for n in primes():
    if n < 100:
        print(n)