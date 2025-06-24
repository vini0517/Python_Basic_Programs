#using Flag
num = 29
# num = int(input("Enter a number: "))

flag = False

if num == 0 or num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

"""
#simple
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, not prime
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

    
#With break and continue
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        return True
    return False

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

"""