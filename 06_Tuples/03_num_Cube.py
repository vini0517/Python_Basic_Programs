#List of Tuples (Number and Cube)

nums = list(map(int, input("Enter numbers: ").split()))
result = [(x, x**3) for x in nums]
print("Result:", result)

# Sample Input: 1 2 3
# Sample Output: [(1, 1), (2, 8), (3, 27)]