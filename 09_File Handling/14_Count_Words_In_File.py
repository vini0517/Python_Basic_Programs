# Program to count the number of words in a text file
# Sample Output: Word Count: 12
filename = input("Enter filename: ")
with open(filename, 'r') as file:
    text = file.read()
print("Word Count:", len(text.split()))