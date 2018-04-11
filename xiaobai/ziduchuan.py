what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_instro = his_name + what_he_does + his_instrument
print(artist_instro)

print(str(1) + '')

print('word' * 3)


word = 'a looooooog word'
num = 12
string = 'Bang!'
total = string * (len(word) - num)
print(total)

name = 'My name is Mike'
print(name[0])
print(name[1:4])
print(name[5:])
print(name[:5])

#找出朋友中的恶魔#
word = 'friends'
find_evil_between_the_freinds = word[0] + word[2:4] + word[-3:-1]
print(find_evil_between_the_freinds)

url = 'http://ww1.site.cn/14e6y3tegdhalkj.jpg'
print(url[-10:])

phoneNumb = '152-0515-2834'
print(phoneNumb.replace(phoneNumb[:9], '*' * 9))

search = '135'

phonea = '135-0875-3456'
phoneb = '153-9873-1352'
print(search + ' is at ' + str(phonea.find(search)) + ' to ' + str(phonea.find(search) + len(search)) + ' in ' + phonea)
print(search + ' is at ' + str(phoneb.find(search)) + ' to ' + str(phoneb.find(search) + len(search)) + ' in ' + phoneb)

print('{} love {}'.format('i', 'you'))
print('{0} love {1}'.format('i', 'you'))








