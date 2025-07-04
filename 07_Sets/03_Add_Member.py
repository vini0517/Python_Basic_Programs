#Add Member(s) to a Set

s = set(input("Enter initial elements: ").split())
s.add(input("Enter element to add: "))
s.update(input("Enter multiple elements to add: ").split())
print("Updated Set:", s)

# Sample Input: 1 2 3 | 4 | 5 6
# Sample Output: {'1', '2', '3', '4', '5', '6'}