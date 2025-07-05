# Program to count the frequency of words in a file
# Sample Output: {'hello': 2, 'world': 1}
from collections import Counter
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    words = file.read().split()
print(Counter(words))