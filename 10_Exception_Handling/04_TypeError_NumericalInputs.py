# Sample Input: abc, 5
# Sample Output: Inputs must be numeric
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Inputs must be numeric")
    print(int(a) + int(b))
except TypeError as e:
    print(e)
