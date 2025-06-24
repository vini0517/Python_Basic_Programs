def find_largest(a, b, c):
    if a >= b and a >= c:
        print(f"The largest number is {a}")
    elif b >= a and b >= c:
        print(f"The largest number is {b}")
    else:
        print(f"The largest number is {c}")

# Example usage
a = 10
b = 25
c = 15
# Or take input: a = float(input("Enter first number: "))
find_largest(a, b, c)
