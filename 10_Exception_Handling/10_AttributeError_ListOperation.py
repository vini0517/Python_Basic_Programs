# Sample Output: 'list' object has no attribute 'upper'
try:
    mylist = ["a", "b"]
    print(mylist.upper())
except AttributeError as e:
    print(e)
