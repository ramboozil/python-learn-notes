passwdlist = ['-*-*', '123456']


def account_login():
    tries= 3
    while tries > 0:
        passwd = input('请输入您的密码：')
        pass_correct = passwdlist[-1] == passwd
        pass_reset = passwdlist[0] == passwd
        if pass_correct:
            print('登录成功！')
            break
        elif pass_reset:
            newpass = input('请输入您的新密码')
            passwdlist.append(newpass)
        else:
            print('您的密码有误，请重新输入！')
            tries = tries - 1
            print('您还有' + str(tries) + '次机会')
    else:
        print('您的账户已被锁定')


account_login()
