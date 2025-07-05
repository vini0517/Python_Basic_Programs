# Program to read a file line by line and store it into a list
# Sample Output: ['line1\n', 'line2\n', ...]
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    lines = file.readlines()
print(lines)
