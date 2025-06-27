#Python Program to Check if a Key is Already Present in a Dictionary
my_dict = {'name': 'Alice', 'age': 25}

key_to_check = 'age'

if key_to_check in my_dict:
    print(f"'{key_to_check}' is present in the dictionary.")
else:
    print(f"'{key_to_check}' is NOT present in the dictionary.")


"""
# 📥 Input Format:
# Enter number of items: 2
# name Alice
# age 25
# Enter key to check: age

my_dict = {}

n = int(input("Enter number of items: "))
for _ in range(n):
    key, value = input().split()
    my_dict[key] = value

key_to_check = input("Enter key to check: ")

if key_to_check in my_dict:
    print(f"'{key_to_check}' is present in the dictionary.")
else:
    print(f"'{key_to_check}' is NOT present in the dictionary.")
"""
