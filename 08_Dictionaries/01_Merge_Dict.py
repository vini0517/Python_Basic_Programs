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

#Concatenate Dictionaries
n = int(input("How many dictionaries? "))
result = {}
for i in range(n):
    d = eval(input(f"Enter dictionary {i+1}: "))
    result.update(d)
print("Concatenated:", result)
# Sample Input: dic1: {1: 10}, dic2: {2: 20}
# Sample Output: {1: 10, 2: 20}
"""