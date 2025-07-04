#Check Superset

a = set(input("Enter elements of A: ").split())
b = set(input("Enter elements of B: ").split())
print("Is A superset of B?", a.issuperset(b))

# Sample Input: 1 2 3 | 1 2
# Sample Output: True