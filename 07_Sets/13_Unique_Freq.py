#Unique Words and Frequency Count

strings = input("Enter words separated by space: ").split()
from collections import Counter
freq = Counter(strings)
print("Frequencies:", dict(freq))

# Sample Input: apple banana apple orange
# Sample Output: {'apple': 2, 'banana': 1, 'orange': 1}