#Find the Largest and Smallest Number in a List
#nums = [10, 5, 20, 8, 3]

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Max:", max(nums))
print("Min:", min(nums))

"""
🧪 Sample Input:
Enter numbers separated by spaces: 4 9 1 12 7

📤 Output Format:
Max: 12
Min: 1

"""