#Remove Item(s) from a Given Set

s = set(input("Enter elements: ").split())
to_remove = input("Enter element to remove: ")
s.remove(to_remove)
print("After remove:", s)

# Sample Input: a b c d | c
# Sample Output: {'a', 'b', 'd'}

"""
#Remove All Elements

s = set(input("Enter elements to clear: ").split())
s.clear()
print("After clear:", s)

# Sample Output: set()
"""