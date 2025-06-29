#Python Program to Check If Two Strings are Anagram
# 📥 Input Format:
# Enter first string: listen
# Enter second string: silent

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")
