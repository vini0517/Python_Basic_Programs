#Find Even and Odd Numbers in a List

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print("Even:", evens)
print("Odd:", odds)

"""
Sample Input:
Enter numbers separated by spaces: 1 2 3 4 5 6

Output Format:
Even: [2, 4, 6]
Odd: [1, 3, 5]

"""