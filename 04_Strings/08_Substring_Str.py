# 📥 Input Format:
# Enter a string: HelloWorld
# Enter start index: 2
# Enter end index: 7

text = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

substring = text[start:end]
print("Substring:", substring)
