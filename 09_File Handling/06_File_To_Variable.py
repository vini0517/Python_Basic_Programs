# Program to read a file line by line and store it into a variable
# Sample Output: Entire file content as string
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    content = file.read()
print(content)