#Remove a Key from a Dictionary

d = eval(input("Enter dictionary: "))
k = input("Enter key to remove: ")
d.pop(k, None)
print("Updated dictionary:", d)
# Sample Input: {'a': 1, 'b': 2}, remove key: 'b'
# Sample Output: {'a': 1}