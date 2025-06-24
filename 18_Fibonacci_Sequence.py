def fibonacci_sequence(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
terms = 10
# terms = int(input("How many terms? "))
fibonacci_sequence(terms)

"""
#Upto n teams
def fibonacci(nterms):
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(f"Fibonacci sequence upto {nterms} term:")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

# Example usage
nterms = int(input("How many terms? "))
fibonacci(nterms)

"""