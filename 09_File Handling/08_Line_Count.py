# Program to count the number of lines in a text file
# Sample Output: Total lines: 5
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    print("Total lines:", sum(1 for _ in file))