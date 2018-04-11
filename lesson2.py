#/usr/bin/env python3
# -*- coding: utf-8 -*-
l=['java','php','python','c++']
print(l[-1])
print(l[-2])
print(len(l))

str = 'java,php,python,c++'
a,b,c,d = str.split(',')
print('\t'.join([a,b,c,d]))

l.append('kotlin')
print(l)
l.insert(2,'c#')
print(l)
l.pop(-1)
print(l)
m=['java','php',['kotlin','c++']]
print(len(m))
print(m[2][0])



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])