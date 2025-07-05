# Program to read an entire file
# Sample Input: sample.txt
# Sample Output: Contents of the file
filename = input("Enter filename to read entire file: ")
with open(filename, 'r') as file:
    print(file.read())
