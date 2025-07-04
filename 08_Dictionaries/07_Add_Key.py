#Add Key to Dictionary

d = eval(input("Enter dictionary: "))
k = input("Enter new key: ")
v = input("Enter value: ")
d[k] = v
print(d)

# Sample Input: {'a': 1, 'b': 2}, new key: 'c', value: 3
# Sample Output: {'a': 1, 'b': 2, 'c': '3'}