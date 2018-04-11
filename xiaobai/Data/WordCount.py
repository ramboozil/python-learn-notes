path = 'C:/Users/miaojie/Downloads/Walden.txt'
with open(path, 'r') as text:
    words = text.read().split()
    set(words)
    print(words)
    for word in words:
        print('{}-{} times'.format(word, words.count(word)))

