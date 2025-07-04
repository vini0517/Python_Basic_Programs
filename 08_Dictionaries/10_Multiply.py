#Multiply All Items in a Dictionary

d = eval(input("Enter dictionary with numeric values: "))
result = 1
for v in d.values():
    result *= v
print("Product:", result)
# Sample Input: {'a': 2, 'b': 3, 'c': 4}
# Sample Output: Product: 24