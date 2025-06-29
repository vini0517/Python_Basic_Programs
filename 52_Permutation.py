#Python Program to Compute All the Permutations of the String

# 📥 Input Format:
# Enter a string: abc

from itertools import permutations

s = input("Enter a string: ")

perm = permutations(s)

print("All permutations:")
for p in perm:
    print(''.join(p))
