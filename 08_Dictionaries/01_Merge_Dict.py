#Python Program to Merge Two Dictionaries

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dict2 into dict1
dict1.update(dict2)

print("Merged dictionary:", dict1)

"""
#1: Using the | Operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)

#2: Using the ** Operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1, **dict_2})
"""