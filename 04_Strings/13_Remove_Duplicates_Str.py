#Remove All Duplicates from a Given String in Python
#Keep Only First Occurrence (Maintain Order)

text = input("Enter a string: ")
result = ""
seen = set()

for char in text:
    if char not in seen:
        seen.add(char)
        result += char
print("String after removing duplicates:", result)
