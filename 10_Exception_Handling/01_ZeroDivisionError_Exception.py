# Sample Input: 10
# Sample Output: Cannot divide by zero.
try:
    num = int(input("Enter a number: "))
    print(num / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
