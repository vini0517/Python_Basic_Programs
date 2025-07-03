#Remove All Duplicates from a List

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique = list(set(nums))
print("Without duplicates:", unique)

"""
Sample Input:
Enter numbers separated by spaces: 1 2 2 3 4 4

Output Format:
Without duplicates: [1, 2, 3, 4]

"""