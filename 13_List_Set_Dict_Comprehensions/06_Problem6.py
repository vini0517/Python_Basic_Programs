# Set Comprehension Problems
#Unique squares from a list

nums = [1, 2, 2, 3, 4, 4]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # {1, 4, 9, 16}
