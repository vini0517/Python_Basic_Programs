#Python Program to Sort a Dictionary by Value
my_dict = {'apple': 10, 'banana': 5, 'cherry': 15}

# Sort by value in ascending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict)

"""
# 📥 Input Format:
# Enter number of items: 3
# Enter key and value separated by space:
# banana 5
# apple 10
# cherry 7

my_dict = {}

n = int(input("Enter number of items: "))
for _ in range(n):
    key, value = input("Enter key and value separated by space: ").split()
    my_dict[key] = int(value)

# Sort by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("\nSorted dictionary by value:")
print(sorted_dict)
"""
