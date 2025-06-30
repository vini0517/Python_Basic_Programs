#Python Program to Iterate Over Dictionaries Using for Loop
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

"""
# 📥 Input Format:
# Enter number of items: 3
# Enter key and value separated by space:
# name Alice
# age 25
# city London

my_dict = {}

n = int(input("Enter number of items: "))
for _ in range(n):
    key, value = input("Enter key and value separated by space: ").split()
    my_dict[key] = value

print("\nDictionary contents:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

"""