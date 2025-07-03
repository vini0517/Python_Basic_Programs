# All Pair Combinations of 2 Tuples

t1 = (1, 2)
t2 = (3, 4)
result = [(a, b) for a in t1 for b in t2]
print("All pair combinations:", result)

# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]