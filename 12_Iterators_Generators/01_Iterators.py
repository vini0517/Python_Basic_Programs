import itertools
import operator

# -----------------------------------------------
# 1. Iterator from Iterables
# Create an iterator from several iterables in a sequence and display the type and elements.
# -----------------------------------------------
print("🔹 1. Iterator from Iterables")

iter1 = iter([1, 2, 3])
iter2 = iter(('a', 'b'))
combined = itertools.chain(iter1, iter2)

print("Type of combined iterator:", type(combined))
print("Elements:", list(combined))

print()

# -----------------------------------------------
# 2. Running Product Iterator
# Generates the running product of elements in an iterable.
# -----------------------------------------------
print("🔹 2. Running Product Iterator")

from functools import reduce

def running_product(iterable):
    product = 1
    for item in iterable:
        product *= item
        yield product

print("Running Product of [2, 3, 4, 5]:", list(running_product([2, 3, 4, 5])))

print()

# -----------------------------------------------
# 3. Max & Min from Iterable
# Generate the max and min values of elements in an iterable.
# -----------------------------------------------
print("🔹 3. Max & Min from Iterable")

data = [4, 7, 1, 9, 0, -2]
print("Max:", max(data))
print("Min:", min(data))

print()

# -----------------------------------------------
# 4. Infinite Iterator with Step
# Infinite iterator returning evenly spaced values.
# -----------------------------------------------
print("🔹 4. Infinite Iterator with Step")

counter = itertools.count(start=10, step=2.5)
print("First 5 values from counter:", [next(counter) for _ in range(5)])

print()

# -----------------------------------------------
# 5. Infinite Cycle of Elements
# Generate an infinite cycle from an iterable.
# -----------------------------------------------
print("🔹 5. Infinite Cycle of Elements")

cycler = itertools.cycle(['A', 'B', 'C'])
print("First 6 cycle values:", [next(cycler) for _ in range(6)])

print()

# -----------------------------------------------
# 6. Drop Until Positive
# Drop elements until one is positive.
# -----------------------------------------------
print("🔹 6. Drop Until Positive")

from itertools import dropwhile

data = [-3, -2, -1, 0, 1, 2, 3]
result = dropwhile(lambda x: x <= 0, data)
print("After dropping non-positive values:", list(result))

print()

# -----------------------------------------------
# 7. Drop While Negative
# Drop elements as long as they are negative; return the rest.
# -----------------------------------------------
print("🔹 7. Drop While Negative")

data = [-5, -3, -1, 0, 2, 4]
result = itertools.dropwhile(lambda x: x < 0, data)
print("After dropping negatives:", list(result))

print()

# -----------------------------------------------
# 8. Consecutive Keys Group
# Group elements with consecutive identical keys.
# -----------------------------------------------
print("🔹 8. Consecutive Keys Group")

data = "aaabbcccddeee"
groups = itertools.groupby(data)
for key, group in groups:
    print(f"Key: {key} -> Group: {list(group)}")

print()

# -----------------------------------------------
# 9. Split Iterable into Chunks
# Split an iterable into n-sized chunks.
# -----------------------------------------------
print("🔹 9. Split Iterable into Chunks")

def chunked(iterable, size):
    it = iter(iterable)
    return iter(lambda: list(itertools.islice(it, size)), [])

data = range(10)
chunks = chunked(data, 3)
print("Chunks of size 3:", list(chunks))

print()

# -----------------------------------------------
# 10. Permutations Iterator
# Create an iterator to get n-length permutations.
# -----------------------------------------------
print("🔹 10. Permutations Iterator")

perm_iter = itertools.permutations([1, 2, 3], 2)
print("Permutations of length 2:", list(perm_iter))


"""
🔹 1. Iterator from Iterables
Type of combined iterator: <class 'itertools.chain'>
Elements: [1, 2, 3, 'a', 'b']

🔹 2. Running Product Iterator
Running Product of [2, 3, 4, 5]: [2, 6, 24, 120]

🔹 3. Max & Min from Iterable
Max: 9
Min: -2

🔹 4. Infinite Iterator with Step
First 5 values from counter: [10, 12.5, 15.0, 17.5, 20.0]

🔹 5. Infinite Cycle of Elements
First 6 cycle values: ['A', 'B', 'C', 'A', 'B', 'C']

🔹 6. Drop Until Positive
After dropping non-positive values: [1, 2, 3]

🔹 7. Drop While Negative
After dropping negatives: [0, 2, 4]

🔹 8. Consecutive Keys Group
Key: a -> Group: ['a', 'a', 'a']
Key: b -> Group: ['b', 'b']
...

🔹 9. Split Iterable into Chunks
Chunks of size 3: [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

🔹 10. Permutations Iterator
Permutations of length 2: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

"""