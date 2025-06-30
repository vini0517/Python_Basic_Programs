def find_divisible_numbers(start, end, divisor):
    print(f"Numbers between {start} and {end} divisible by {divisor}:")
    for num in range(start, end + 1):
        if num % divisor == 0:
            print(num)

# Example usage
start = 1
end = 100
divisor = 7
# You can also use input() to get values from the user

find_divisible_numbers(start, end, divisor)

"""
# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are",result)

"""