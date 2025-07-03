#Modulo of Tuple Elements

t = tuple(map(int, input("Enter tuple: ").split()))
m = int(input("Modulo with: "))
print("Modulo result:", tuple(x % m for x in t))

# Sample Input: 10 25 30 | 6
# Sample Output: (4, 1, 0)