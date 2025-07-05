# Sample Input: (try a file with restricted permission)
# Sample Output: Permission denied to read file.
filename = input("Enter filename: ")
try:
    with open(filename, 'r') as f:
        print(f.read())
except PermissionError:
    print("Permission denied to read file.")
