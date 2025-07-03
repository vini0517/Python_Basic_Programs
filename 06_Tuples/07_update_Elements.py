#Update Each Element in Tuple List

tuple_list = [(1, 2), (3, 4)]
result = [(a+1, b+1) for (a, b) in tuple_list]
print("Updated List:", result)

# Output: [(2, 3), (4, 5)]