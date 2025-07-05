# Program to assess if a file is closed or not
# Sample Output: Closed? False \n Closed after closing? True
filename = input("Enter filename: ")
f = open(filename, 'r')
print("Closed?", f.closed)
f.close()
print("Closed after closing?", f.closed)
