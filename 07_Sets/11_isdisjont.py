#No Common Elements

a = set(input("Enter elements of set A: ").split())
b = set(input("Enter elements of set B: ").split())
print("Disjoint:", a.isdisjoint(b))

# Sample Input: 1 2 | 3 4
# Sample Output: True