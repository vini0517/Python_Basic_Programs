#Python Program to Remove Punctuations From a String
import string

# Input string
input_str = "Hello!!! How are you? I'm fine; thank you."

# Define punctuation characters
punctuations = string.punctuation

# Remove punctuation from the string
no_punct = ""
for char in input_str:
    if char not in punctuations:
        no_punct += char

print("Original String: ", input_str)
print("String without punctuation: ", no_punct)
