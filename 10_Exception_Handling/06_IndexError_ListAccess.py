# Sample Input: 5
# Sample Output: Index out of range.
my_list = [1, 2, 3]
try:
    index = int(input("Enter index to access: "))
    print(my_list[index])
except IndexError:
    print("Index out of range.")
