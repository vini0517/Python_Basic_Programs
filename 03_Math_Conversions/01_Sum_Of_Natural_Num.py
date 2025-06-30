def sum_of_natural_numbers(n):
    return n * (n + 1) // 2  # Using the formula: n(n + 1)/2

# Example usage
num = 10
# num = int(input("Enter a positive number: "))

if num < 1:
    print("Please enter a positive number")
else:
    total = sum_of_natural_numbers(num)
    print(f"The sum of natural numbers up to {num} is {total}")

"""
def sum_natural(num):
    if num < 0:
        print("Enter a positive number")
    else:
        Sum = 0
        while num > 0:
            Sum += num
            num -= 1
        print(f"The sum is {Sum}")

# Example usage
sum_natural(16)
# Or use input: sum_natural(int(input("Enter a positive number: ")))

"""