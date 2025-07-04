#Shallow Copy of a Set

original = set(input("Enter elements: ").split())
copy_set = original.copy()
print("Copy:", copy_set)

# Sample Input: x y z
# Sample Output: {'x', 'y', 'z'}