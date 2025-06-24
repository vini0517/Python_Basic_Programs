def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == number

# Example usage
num = 153
# num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

"""
#3-digit: 153, 370, 371, 407,....4-digit: 9474
$153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

"""