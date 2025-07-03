#Join Tuples with Similar Initial Element

data = [(1, 'a'), (2, 'b'), (1, 'c')]
from collections import defaultdict
merged = defaultdict(list)
for key, val in data:
    merged[key].append(val)
print("Joined Tuples:", dict(merged))

# Output: {1: ['a', 'c'], 2: ['b']}