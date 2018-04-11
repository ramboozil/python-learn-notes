from functools import reduce


def str2num(s):
    s1 = s.split('.')
    if len(s1) == 1:
        return int(s1[0])
    else:
        return int(s1[0]) + (reduce(lambda x, y: x / 10 + y, map(int, s1[1][::-1]))) / 10


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.0016')
    print('99 + 88 + 7.6 =', r)


main()
