def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == number

def find_armstrong_in_range(lower, upper):
    print(f"Armstrong numbers between {lower} and {upper}:")
    for num in range(lower, upper + 1):
        if is_armstrong(num):
            print(num)

# Example usage
lower = 100
upper = 1000
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
find_armstrong_in_range(lower, upper)
