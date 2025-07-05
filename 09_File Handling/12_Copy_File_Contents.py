# Program to copy the contents of a file to another file
# Sample Output: Copied successfully.
src = input("Enter source filename: ")
dest = input("Enter destination filename: ")
with open(src, 'r') as f1, open(dest, 'w') as f2:
    f2.write(f1.read())
print("Copied successfully.")