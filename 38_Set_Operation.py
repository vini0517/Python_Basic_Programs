#Python Program to Illustrate Different Set Operations

# Define two example sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print("Union of A and B:", A | B)

# Intersection
print("Intersection of A and B:", A & B)

# Difference (A - B)
print("Difference of A and B (A - B):", A - B)

# Difference (B - A)
print("Difference of B and A (B - A):", B - A)

# Symmetric Difference
print("Symmetric Difference of A and B:", A ^ B)


"""
A | B → union of both sets

A & B → common elements

A - B → items in A but not in B

A ^ B → items in A or B but not both
"""