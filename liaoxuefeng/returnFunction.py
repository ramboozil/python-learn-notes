def createCounter():
    n = 0

    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

f = [0]
print(f[0] + 1)