#my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Remove key 'age'
del my_dict['age']

print(my_dict)

"""
# 📥 Input Format:
# Enter number of items: 2
# name Alice
# age 25
# Enter key to delete: age

my_dict = {}

n = int(input("Enter number of items: "))
for _ in range(n):
    key, value = input().split()
    my_dict[key] = value

key_to_delete = input("Enter key to delete: ")

if key_to_delete in my_dict:
    del my_dict[key_to_delete]
    print(f"'{key_to_delete}' has been deleted.")
else:
    print(f"'{key_to_delete}' not found.")

print("Updated dictionary:", my_dict)
"""