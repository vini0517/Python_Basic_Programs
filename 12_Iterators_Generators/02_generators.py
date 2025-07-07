import random
import math
import itertools

# 1. Cubes Generator
def generate_cubes(n):
    for i in range(1, n + 1):
        yield i ** 3

# 2. Random Number Generator
def random_number_generator(low, high, count):
    for _ in range(count):
        yield random.randint(low, high)

# 3. Prime Generator (Range)
def prime_generator(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                yield num

# 4. Fibonacci Generator
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 5. List Permutations Generator
def list_permutations(lst):
    yield from itertools.permutations(lst)

# 6. Combinations Generator
def list_combinations(lst, r):
    yield from itertools.combinations(lst, r)

# 7. Collatz Sequence Generator
def collatz_sequence(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

# 8. Next Palindrome Generator
def next_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    while True:
        n += 1
        if is_palindrome(n):
            yield n

# 9. Prime Factors Generator
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

# 10. Prime Generator (Duplicate Variation)
def prime_generator_v2(start, end):
    yield from prime_generator(start, end)

# 11. String Permutations Generator
def string_permutations(s):
    yield from map("".join, itertools.permutations(s))

# 12. Next Happy Number Generator
def next_happy_number(n):
    def is_happy(num):
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = sum(int(i) ** 2 for i in str(num))
        return num == 1
    while True:
        n += 1
        if is_happy(n):
            yield n

# 13. Square and Cube Roots Generator
def roots_generator(n):
    for i in range(1, n + 1):
        yield (i, round(i ** 0.5, 3), round(i ** (1 / 3), 3))

# 14. Next Armstrong Number Generator
def next_armstrong(n):
    def is_armstrong(num):
        digits = str(num)
        power = len(digits)
        return sum(int(d) ** power for d in digits) == num
    while True:
        n += 1
        if is_armstrong(n):
            yield n

# 15. Factors Generator
def factors_gen(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

# 16. Running Average Generator
def running_average_gen():
    total = 0
    count = 0
    while True:
        num = yield None if count == 0 else total / count
        total += num
        count += 1

# 17. Powers Generator
def powers_gen(base, max_exp):
    for exp in range(max_exp + 1):
        yield base ** exp

# -----------------------
# 🔍 Sample Demonstration
# -----------------------
if __name__ == "__main__":
    print("1. Cubes of 1 to 5:", list(generate_cubes(5)))
    
    print("2. Random numbers between 10 and 20:", list(random_number_generator(10, 20, 5)))
    
    print("3. Prime numbers between 10 and 30:", list(prime_generator(10, 30)))
    
    fib = fibonacci_gen()
    print("4. First 5 Fibonacci numbers:", [next(fib) for _ in range(5)])
    
    print("5. Permutations of [1, 2, 3]:", list(list_permutations([1, 2, 3])))
    
    print("6. Combinations of [1, 2, 3] taken 2:", list(list_combinations([1, 2, 3], 2)))
    
    print("7. Collatz sequence of 13:", list(collatz_sequence(13)))
    
    pal_gen = next_palindrome(123)
    print("8. Next 3 palindrome numbers after 123:", [next(pal_gen) for _ in range(3)])
    
    print("9. Prime factors of 60:", list(prime_factors(60)))
    
    print("10. Duplicate Prime Gen 50-60:", list(prime_generator_v2(50, 60)))
    
    print("11. String permutations of 'abc':", list(string_permutations("abc")))
    
    happy = next_happy_number(10)
    print("12. Next 3 happy numbers after 10:", [next(happy) for _ in range(3)])
    
    print("13. Square and cube roots of 1 to 5:", list(roots_generator(5)))
    
    arm_gen = next_armstrong(150)
    print("14. Next 3 Armstrong numbers after 150:", [next(arm_gen) for _ in range(3)])
    
    print("15. Factors of 28:", list(factors_gen(28)))
    
    print("16. Running average of [10, 20, 30]:")
    avg = running_average_gen()
    next(avg)  # Prime the generator
    print(avg.send(10))  # 10.0
    print(avg.send(20))  # 15.0
    print(avg.send(30))  # 20.0
    
    print("17. Powers of 2 up to exponent 5:", list(powers_gen(2, 5)))
