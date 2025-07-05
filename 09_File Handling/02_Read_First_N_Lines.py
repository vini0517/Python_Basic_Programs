# Program to read first n lines of a file
# Sample Input: sample.txt, n = 3
# Sample Output: First 3 lines of the file
filename = input("Enter filename: ")
n = int(input("Enter number of lines: "))
with open(filename, 'r') as file:
    for i in range(n):
        print(file.readline(), end='')