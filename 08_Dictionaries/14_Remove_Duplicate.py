#Remove Duplicates from the Dictionary

d = eval(input("Enter dictionary: "))
res = {}
for k, v in d.items():
    if v not in res.values():
        res[k] = v
print("After removing duplicates:", res)
# Sample Input: {'a': 1, 'b': 2, 'c': 1}
# Sample Output: {'a': 1, 'b': 2}
