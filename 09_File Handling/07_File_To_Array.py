# Program to read a file line by line and store it into an array
# Sample Output: ['line1', 'line2', ...]
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    array = [line.strip() for line in file]
print(array)