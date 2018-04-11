import string

path = 'C:/Users/miaojie/Downloads/Walden.txt'
with open(path, 'r') as text:
    words = [raw_words.strip(string.punctuation) for raw_words in text.read().split()]
    word_index = set(words)
    count_dict = {word: words.count(word) for word in word_index}
for index in sorted(count_dict, key=lambda x: count_dict[x], reverse=True):
    print('{} - {}'.format(index, count_dict[index]))
