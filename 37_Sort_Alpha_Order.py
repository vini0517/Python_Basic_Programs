# Get input from user
input_str = input("Enter a sentence: ")

# Split the sentence into words
words = input_str.split()

# Sort alphabetically (case-insensitive)
words.sort(key=str.lower)

# Print the result
print("Words in alphabetical order:")
for word in words:
    print(word)
