# Program to get the file size of a plain file
# Sample Output: File size in bytes: 124
import os
filename = input("Enter filename: ")
print("File size in bytes:", os.path.getsize(filename))