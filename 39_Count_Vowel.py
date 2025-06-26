#Python Program to Count the Number of Each Vowel
# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)

"""
ip_str = 'Hello, have you tried our tutorial section yet?'

Vowel count::
{'a': 2, 'e': 3, 'i': 2, 'o': 3, 'u': 3}

"""