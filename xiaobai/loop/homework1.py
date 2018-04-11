def create_file():
    for i in range(1, 11):
        with open('C:/Users/miaojie/Desktop/caiji/' + str(i) + '.txt', 'w') as text:
            text.write(str(i))
            text.close()
        print('done')


create_file()