# Maximum and Minimum K Elements in Tuple


t = tuple(map(int, input("Enter tuple elements: ").split()))
k = int(input("Enter value of K: "))
sorted_t = sorted(t)
print("Minimum", k, "elements:", sorted_t[:k])
print("Maximum", k, "elements:", sorted_t[-k:])


# Sample Input: 5 2 8 6 3 | 2
# Sample Output: Minimum 2 elements: [2, 3] | Maximum 2 elements: [6, 8]