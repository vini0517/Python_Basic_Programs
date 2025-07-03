# Elements Frequency in Tuple

t = (1, 2, 2, 3, 1, 1)
from collections import Counter
print("Frequencies:", dict(Counter(t)))
# Output: {1: 3, 2: 2, 3: 1}

"""
#Assign Frequency to Tuples
tuples = [(1, 2), (3, 4), (1, 2), (3, 4), (5, 6)]
from collections import Counter
freq = Counter(tuples)
print("Tuple Frequencies:", dict(freq))
# Output: {(1, 2): 2, (3, 4): 2, (5, 6): 1}
"""