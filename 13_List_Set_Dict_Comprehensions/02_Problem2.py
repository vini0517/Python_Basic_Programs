#Even numbers from a list

nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)  # [2, 4, 6]
