# Function to find HCF using Euclidean algorithm
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to find LCM
def compute_lcm(x, y):
    hcf = compute_hcf(x, y)
    return (x * y) // hcf

# Example usage
num1 = 12
num2 = 18

lcm = compute_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm)

"""
# Function to calculate the HCF using Euclidean Algorithm
def compute_hcf(x, y):
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

# Function to calculate the LCM using the relation: LCM = (x * y) / HCF
def compute_lcm(x, y):
    hcf = compute_hcf(x, y)
    lcm = (x * y) // hcf
    return lcm

# Example numbers
num1 = 60
num2 = 48

# You can also use user input like this:
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

print("First number is:", num1)
print("Second number is:", num2)

hcf_result = compute_hcf(num1, num2)
lcm_result = compute_lcm(num1, num2)

print("The HCF of", num1, "and", num2, "is", hcf_result)
print("The LCM of", num1, "and", num2, "is", lcm_result)

"""