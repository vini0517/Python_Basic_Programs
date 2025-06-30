def print_multiplication_table(num):
    print(f"Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Example usage
num = 7
# num = int(input("Enter a number: "))
print_multiplication_table(num)
