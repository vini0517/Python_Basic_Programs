#Sort a List in Ascending and Descending Order

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))

"""
Sample Input:
Enter numbers separated by spaces: 5 1 9 3

Output Format:
Ascending: [1, 3, 5, 9]
Descending: [9, 5, 3, 1]

"""