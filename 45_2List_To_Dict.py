# Python Program to Convert Two Lists Into a Dictionary

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Use zip() to pair keys and values
my_dict = dict(zip(keys, values))

print(my_dict)


"""
# 📥 Input Format:
# Enter comma-separated keys: name,age,city
# Enter comma-separated values: Alice,25,London

keys = input("Enter comma-separated keys: ").split(",")
values = input("Enter comma-separated values: ").split(",")

if len(keys) != len(values):
    print("Error: Keys and values must have the same number of elements.")
else:
    my_dict = dict(zip(keys, values))
    print("Combined dictionary:", my_dict)
"""