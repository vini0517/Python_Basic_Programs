# Program to read last n lines of a file
# Sample Input: sample.txt, n = 2
# Sample Output: Last 2 lines of the file
from collections import deque
filename = input("Enter filename: ")
n = int(input("Enter number of last lines: "))
with open(filename, 'r') as file:
    print(''.join(deque(file, n)))