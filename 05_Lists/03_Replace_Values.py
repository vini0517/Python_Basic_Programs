#Replace Multiple Values
nums = input("Enter 5 numbers: ").split()
nums[1:4] = ['20', '30', '40']
print("Replaced list:", nums)

# Input: 1 2 3 4 5
# Output: ['1', '20', '30', '40', '5']
