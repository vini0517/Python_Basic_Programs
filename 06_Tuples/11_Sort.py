#Sort a List of Tuples by Second Item

lst = [(1, 3), (2, 1), (3, 2)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print("Sorted by second item:", sorted_lst)
# Output: [(2, 1), (3, 2), (1, 3)]

"""
#Sort Tuples by Total Digits

lst = [(123,), (1,), (22,)]
sorted_lst = sorted(lst, key=lambda x: len(str(x[0])))
print("Sorted by digits:", sorted_lst)
# Output: [(1,), (22,), (123,)]
"""