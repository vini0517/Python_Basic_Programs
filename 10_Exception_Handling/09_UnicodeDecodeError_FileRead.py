# Sample Input: (Open binary or wrongly encoded file)
# Sample Output: Cannot decode file content due to encoding issue.
filename = input("Enter filename: ")
try:
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
except UnicodeDecodeError:
    print("Cannot decode file content due to encoding issue.")
