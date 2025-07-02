list1 = input("Enter first list: ").split()
list2 = input("Enter second list to extend: ").split()

list1.extend(list2)
print("After extend:", list1)

# Input1: 1 2
# Input2: 3 4
# Output: ['1', '2', '3', '4']
