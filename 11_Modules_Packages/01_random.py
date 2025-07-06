import random
import string
import os
from datetime import datetime, timedelta

# -----------------------------------------------
# 1. Random Value Generation
# Write a Python program to generate a random color hex, a random alphabetical string,
# random value between two integers (inclusive), and a random multiple of 7 between 0 and 70.
# Use random.randint()
# -----------------------------------------------
print("🔹 1. Random Value Generation")
color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
alpha_string = ''.join(random.choices(string.ascii_letters, k=8))
rand_int = random.randint(10, 50)
multiple_of_7 = random.randint(0, 10) * 7

print("Random Color Hex:", color)
print("Random Alphabetical String:", alpha_string)
print("Random Integer (10–50):", rand_int)
print("Random Multiple of 7 (0–70):", multiple_of_7)
print()

# -----------------------------------------------
# 2. Random Element Selection
# Write a Python program to select a random element from a list, set,
# dictionary value, and file from a directory. Use random.choice()
# -----------------------------------------------
print("🔹 2. Random Element Selection")
my_list = [1, 2, 3, 4, 5]
my_set = {'apple', 'banana', 'cherry'}
my_dict = {'a': 10, 'b': 20, 'c': 30}
directory = "."  # current working directory

print("Random from list:", random.choice(my_list))
print("Random from set:", random.choice(list(my_set)))
print("Random from dict values:", random.choice(list(my_dict.values())))
print("Random file from directory:", random.choice(os.listdir(directory)))
print()

# -----------------------------------------------
# 3. Random Alphabetical Generation
# Write a Python program that generates random alphabetical characters,
# alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()
# -----------------------------------------------
print("🔹 3. Random Alphabetical Generation")
rand_char = random.choice(string.ascii_letters)
rand_str = ''.join(random.choices(string.ascii_letters, k=6))
fixed_len_str = ''.join(random.choices(string.ascii_letters, k=10))

print("Random Character:", rand_char)
print("Random String:", rand_str)
print("Fixed Length String (10):", fixed_len_str)
print()

# -----------------------------------------------
# 4. Seeded Random Float Generation
# Write a Python program to construct a seeded random number generator,
# also generate a float between 0 and 1, excluding 1. Use random.random()
# -----------------------------------------------
print("🔹 4. Seeded Random Float Generation")
random.seed(42)
print("Seeded Random Float [0,1):", random.random())
print()

# -----------------------------------------------
# 5. Random Integer and Date with randrange
# Write a Python program to generate a random integer between 0 and 6 - excluding 6,
# random integer between 5 and 10 - excluding 10,
# random integer between 0 and 10 with step 3,
# and random date between two dates. Use random.randrange()
# -----------------------------------------------
print("🔹 5. Random Integer and Date with randrange")
print("Random int (0–5):", random.randrange(0, 6))
print("Random int (5–9):", random.randrange(5, 10))
print("Random int (0–10, step=3):", random.randrange(0, 11, 3))

start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)
delta_days = (end_date - start_date).days
rand_day_offset = random.randrange(delta_days)
rand_date = start_date + timedelta(days=rand_day_offset)
print("Random Date:", rand_date.date())
print()

# -----------------------------------------------
# 6. List Shuffle
# Write a Python program to shuffle the elements of a given list. Use random.shuffle()
# -----------------------------------------------
print("🔹 6. List Shuffle")
shuffle_list = [10, 20, 30, 40, 50]
random.shuffle(shuffle_list)
print("Shuffled List:", shuffle_list)
print()

# -----------------------------------------------
# 7. Uniform Random Float Generation
# Write a Python program to generate a float between 0 and 1, inclusive
# and generate a random float within a specific range. Use random.uniform()
# -----------------------------------------------
print("🔹 7. Uniform Random Float Generation")
print("Random Float [0,1]:", random.uniform(0, 1))
print("Random Float [10.5–25.5]:", random.uniform(10.5, 25.5))
print()

# -----------------------------------------------
# 8. Random Sample from List
# Write a Python program to create a list of random integers and randomly
# select multiple items from the said list. Use random.sample()
# -----------------------------------------------
print("🔹 8. Random Sample from List")
sample_list = list(range(1, 21))
sample = random.sample(sample_list, 5)
print("Random Sample (5 elements):", sample)
print()

# -----------------------------------------------
# 9. Set Seed and Random Float
# Write a Python program to set a random seed and get a random number between 0 and 1.
# Use random.random()
# -----------------------------------------------
print("🔹 9. Set Seed and Random Float")
random.seed(100)
print("Seeded Random Float:", random.random())
print()
