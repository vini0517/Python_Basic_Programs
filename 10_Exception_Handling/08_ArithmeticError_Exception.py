# Sample Input: 10, 0
# Sample Output: Arithmetic error occurred.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ArithmeticError:
    print("Arithmetic error occurred.")
