#1. Using a Temporary Variable
x = 5
y = 10

temp = x
x = y
y = temp

print(f'The value of x after swapping: {x}')
print(f'The value of y after swapping: {y}')

"""
#2. Without Temporary Variable (Tuple Unpacking)
x = 5
y = 10

x, y = y, x

print(f'x = {x}')
print(f'y = {y}')

#3. Using Addition and Subtraction
x = 5
y = 10

x = x + y
y = x - y
x = x - y

print(f'x = {x}')
print(f'y = {y}')

#4. Using Multiplication and Division 
#(Make sure x and y are not zero)
x = 5
y = 10

x = x * y
y = x / y
x = x / y

print(f'x = {x}')
print(f'y = {y}')

# 5. Using XOR (Integers Only)
x = 5
y = 10

x = x ^ y
y = x ^ y
x = x ^ y

print(f'x = {x}')
print(f'y = {y}')

"""
