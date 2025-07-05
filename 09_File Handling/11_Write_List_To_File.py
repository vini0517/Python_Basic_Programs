# Program to write a list to a file
# Sample Input: ['apple', 'banana'], filename = fruits.txt
# Sample Output: File written with each item on new line
lines = input("Enter list items separated by comma: ").split(',')
filename = input("Enter filename: ")
with open(filename, 'w') as file:
    for item in lines:
        file.write(item.strip() + '\n')