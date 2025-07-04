#Check Subset

a = set(input("Enter set A: ").split())
b = set(input("Enter set B: ").split())
print("Is A subset of B?", a.issubset(b))

# Sample Input: 1 2 | 1 2 3
# Sample Output: True