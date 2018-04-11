def file_create(name, msg):
    path = 'C:/Users/miaojie/Desktop/caiji/'
    full_path = path + name + '.txt'
    file = open(full_path, 'w')
    cleanmsg = text_filter(msg)
    file.write(cleanmsg)
    file.close()
    print('done')


def text_filter(msg, oldstr ='lame', newstr ='awesome'):
    return msg.replace(oldstr, newstr)


file_create('try', 'lame!lame!lame!')
