class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self # 返回自身这个的对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回当前对象下一个值


for n in Fib():
    print(n)

# print(Fib()[1]) 要实现[] 得重写__getItem()__
