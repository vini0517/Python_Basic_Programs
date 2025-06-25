# Function to find HCF/GCD
def find_hcf(x, y):
    # Choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x

    # Check from 1 to the smaller number
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i  # Update HCF if both numbers are divisible
    return hcf

# Example input
num1 = 54
num2 = 24

# Call the function
result = find_hcf(num1, num2)

# Display the result
print(f"The HCF of {num1} and {num2} is {result}")
#print("The LCM of", num1, "and", num2, "is", lcm)

"""
#2
def find_hcf(x, y):
    hcf = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

# Example
num1 = 54
num2 = 24

print(f"The HCF of {num1} and {num2} is {find_hcf(num1, num2)}")

#3: Using the Euclidean Algorithm
# Function to find HCF using Euclidean algorithm
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Example usage
hcf = compute_hcf(300, 400)
print(f"The HCF is {hcf}")

"""