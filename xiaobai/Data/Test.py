set = {1, 2, 3, 4, 5}
set.discard(5)
print(set)

ta = [1, 2, 3]
tb = [9, 8, 7]
tc = ['a', 'b', 'c']
for (a, b, c) in zip(ta, tb, tc):
    print(a, c)


a = []
for i in range(1, 11):
    a.append(i)
print(a)

b = [i for i in range(1, 11)]
print(b)

a = [i ** 2 for i in range(1, 11)]
print(a)

b = [j + 1 for j in range(1, 11)]
print(b)

c = [k for k in range(1, 11) if k % 2 == 0]
print(c)

d = [letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(d)

#字典推导式
d = {i: i + 1 for i in range(4)}
print(d)
g = {i: j for i, j in zip(range(1, 6), 'abcde')}
print(g)
g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
print(g)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(0, len(letters)-1):
    print(i, letters[i])

for index, letter in enumerate(letters):
    print(index, letter)


