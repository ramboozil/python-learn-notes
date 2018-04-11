from liaoxuefeng.command import MyObject

o = MyObject(10)


def run(x):
    inp = input('method >>')
    if hasattr(o, inp):
        func = getattr(o, inp)
        return func()
    else:
        setattr(o, inp, lambda x: x**2)
        func = getattr(o, inp)
        return func(x)


if __name__ == '__main__':
    print(run(5))