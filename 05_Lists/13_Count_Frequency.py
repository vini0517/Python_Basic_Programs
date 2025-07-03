#Count Frequency of Each Element

from collections import Counter
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Frequencies:", dict(Counter(nums)))

"""
Sample Input:
Enter numbers separated by spaces: 1 2 2 3 3 3

Output Format:
Frequencies: {1: 1, 2: 2, 3: 3}

"""