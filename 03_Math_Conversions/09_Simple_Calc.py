# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Display menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if choice == '1':
    print("Result is:", add(num1, num2))
elif choice == '2':
    print("Result is:", subtract(num1, num2))
elif choice == '3':
    print("Result is:", multiply(num1, num2))
elif choice == '4':
    print("Result is:", divide(num1, num2))
else:
    print("Invalid input")
