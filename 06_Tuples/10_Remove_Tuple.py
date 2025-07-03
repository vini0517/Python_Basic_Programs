#Remove Tuples of Length K

lst = [(1,), (1, 2), (3, 4, 5)]
k = 2
filtered = [t for t in lst if len(t) != k]
print("Filtered List:", filtered)

# Output: [(1,), (3, 4, 5)]

"""
#Remove Tuples Where All Elements Are None

lst = [(None, None), (1, None), (2, 3)]
filtered = [t for t in lst if any(e is not None for e in t)]
print("Cleaned List:", filtered)

# Output: [(1, None), (2, 3)]
"""