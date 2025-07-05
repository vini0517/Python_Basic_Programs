# Sample Input: abc
# Sample Output: Invalid input! Not an integer.
try:
    value = int(input("Enter an integer: "))
    print("You entered:", value)
except ValueError:
    print("Invalid input! Not an integer.")
