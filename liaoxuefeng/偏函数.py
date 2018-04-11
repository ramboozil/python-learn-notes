import functools

i = int('1010', 2)
print(i)

int2 = functools.partial(int, base=2)   # def int2(x, base = 2) return int(x, base)
print(int2('1010', base = 10))


kw = {'base': 2}
print(int('10010', kw['base']))