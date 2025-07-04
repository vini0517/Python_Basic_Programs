#Generate Dictionary of Numbers and Their Squares

n = int(input("Enter n: "))
squares = {x: x*x for x in range(1, n+1)}
print(squares)

# Sample Input: 5
# Sample Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
