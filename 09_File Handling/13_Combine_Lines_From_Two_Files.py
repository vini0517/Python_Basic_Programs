# Program to combine each line from first file with the corresponding line in second file
# Sample Output: Line1_from_f1 Line1_from_f2
f1 = input("Enter first filename: ")
f2 = input("Enter second filename: ")
with open(f1, 'r') as file1, open(f2, 'r') as file2:
    for line1, line2 in zip(file1, file2):
        print(line1.strip() + ' ' + line2.strip())