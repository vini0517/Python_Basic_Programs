def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
# num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

"""
#Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = 5
# num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")

"""