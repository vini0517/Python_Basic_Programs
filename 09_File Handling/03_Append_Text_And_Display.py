# Program to append text to a file and display the text
# Sample Input: filename = notes.txt, text = Hello World
# Sample Output: Displays all contents of file after appending
filename = input("Enter filename: ")
text = input("Enter text to append: ")
with open(filename, 'a') as file:
    file.write(text + "\n")
with open(filename, 'r') as file:
    print(file.read())