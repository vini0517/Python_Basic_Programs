#Print All Distinct Values in a Dictionary

data = eval(input("Enter list of dictionaries: "))
values = set()
for d in data:
    values.update(d.values())
print("Unique Values:", values)
# Sample Input: [{"V": "S001"}, {"VI": "S002"}, {"V": "S001"}]
# Sample Output: {'S001', 'S002'}
