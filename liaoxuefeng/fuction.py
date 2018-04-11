def add(x, y, f):
    return f(x) + f(y)


result = add(-5, 6, abs)
print(result)
