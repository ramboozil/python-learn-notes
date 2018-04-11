from functools import reduce


def is_palindrome(n):
    st = str(n)
    # if st == st[::-1]:   写法1
    if st == reduce(lambda x, y: y + x, st):              # 写法2
        return st


output = filter(is_palindrome, range(1, 100))
print('1~1000:', list(output))
