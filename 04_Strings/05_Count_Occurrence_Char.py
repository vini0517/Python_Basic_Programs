# Python Program to Count the Number of Occurrence of a Character in String

# 📥 Input Format:
# Enter string: banana
# Enter character to count: a

text = input("Enter string: ")
char = input("Enter character to count: ")

count = text.count(char)
print(f"'{char}' occurs {count} times.")
