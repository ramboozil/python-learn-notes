from liaoxuefeng.command import MyObject


myComputer = MyObject()


def run():
    inp = input('输入你要测试的函数名字')
    if inp == 'sum':
        return myComputer.sum()
    elif inp == 'plus':
        return myComputer.plus()
    else:
        print('not found')


if __name__ == '__main__':
    print(run())