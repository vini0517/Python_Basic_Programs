#Count frequency of characters in a word

word = 'banana'
freq = {char: word.count(char) for char in set(word)}
print(freq)  # {'b': 1, 'a': 3, 'n': 2}
