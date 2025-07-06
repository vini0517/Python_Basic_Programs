import copy

# -----------------------------------------------
# 1. Shallow Copy of List
# Write a Python program to create a shallow copy of a given list. Use copy.copy
# -----------------------------------------------
print("🔹 1. Shallow Copy of List")

original_list = [1, 2, [3, 4]]
shallow_copy_list = copy.copy(original_list)

print("Original List:", original_list)
print("Shallow Copy:", shallow_copy_list)

# Modifying inner list
original_list[2][0] = 99
print("After modifying original inner list:")
print("Original List:", original_list)
print("Shallow Copy (affected):", shallow_copy_list)

print()

# -----------------------------------------------
# 2. Deep Copy of List
# Write a Python program to create a deep copy of a given list. Use copy.deepcopy
# -----------------------------------------------
print("🔹 2. Deep Copy of List")

original_list = [1, 2, [3, 4]]
deep_copy_list = copy.deepcopy(original_list)

print("Original List:", original_list)
print("Deep Copy:", deep_copy_list)

# Modifying inner list
original_list[2][0] = 88
print("After modifying original inner list:")
print("Original List:", original_list)
print("Deep Copy (not affected):", deep_copy_list)

print()

# -----------------------------------------------
# 3. Shallow Copy of Dictionary
# Write a Python program to create a shallow copy of a given dictionary. Use copy.copy
# -----------------------------------------------
print("🔹 3. Shallow Copy of Dictionary")

original_dict = {'a': 1, 'b': {'x': 10, 'y': 20}}
shallow_copy_dict = copy.copy(original_dict)

print("Original Dict:", original_dict)
print("Shallow Copy:", shallow_copy_dict)

# Modifying nested dictionary
original_dict['b']['x'] = 99
print("After modifying original nested dict:")
print("Original Dict:", original_dict)
print("Shallow Copy (affected):", shallow_copy_dict)

print()

# -----------------------------------------------
# 4. Deep Copy of Dictionary
# Write a Python program to create a deep copy of a given dictionary. Use copy.deepcopy
# -----------------------------------------------
print("🔹 4. Deep Copy of Dictionary")

original_dict = {'a': 1, 'b': {'x': 10, 'y': 20}}
deep_copy_dict = copy.deepcopy(original_dict)

print("Original Dict:", original_dict)
print("Deep Copy:", deep_copy_dict)

# Modifying nested dictionary
original_dict['b']['x'] = 77
print("After modifying original nested dict:")
print("Original Dict:", original_dict)
print("Deep Copy (not affected):", deep_copy_dict)

print()

"""
🔹 1. Shallow Copy of List
Original List: [1, 2, [3, 4]]
Shallow Copy: [1, 2, [3, 4]]
After modifying original inner list:
Original List: [1, 2, [99, 4]]
Shallow Copy (affected): [1, 2, [99, 4]]

🔹 2. Deep Copy of List
Original List: [1, 2, [3, 4]]
Deep Copy: [1, 2, [3, 4]]
After modifying original inner list:
Original List: [1, 2, [88, 4]]
Deep Copy (not affected): [1, 2, [3, 4]]

🔹 3. Shallow Copy of Dictionary
Original Dict: {'a': 1, 'b': {'x': 10, 'y': 20}}
Shallow Copy: {'a': 1, 'b': {'x': 10, 'y': 20}}
After modifying original nested dict:
Original Dict: {'a': 1, 'b': {'x': 99, 'y': 20}}
Shallow Copy (affected): {'a': 1, 'b': {'x': 99, 'y': 20}}

🔹 4. Deep Copy of Dictionary
Original Dict: {'a': 1, 'b': {'x': 10, 'y': 20}}
Deep Copy: {'a': 1, 'b': {'x': 10, 'y': 20}}
After modifying original nested dict:
Original Dict: {'a': 1, 'b': {'x': 77, 'y': 20}}
Deep Copy (not affected): {'a': 1, 'b': {'x': 10, 'y': 20}}

"""