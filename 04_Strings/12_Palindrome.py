#Python Program to Check Whether a String is Palindrome or Not

my_str = 'aIbohPhoBiA'
if my_str.casefold() == my_str.casefold()[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""
my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()        # Converts to lowercase: 'aibohphobia'
rev_str = reversed(my_str)        # Returns a reversed iterator

if list(my_str) == list(rev_str): # Compares original list to reversed list
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""