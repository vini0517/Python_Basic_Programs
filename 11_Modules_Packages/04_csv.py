import csv
import io
import os

# Make sure a sample CSV file exists
sample_csv_path = "sample.csv"
with open(sample_csv_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", "30", "New York"])
    writer.writerow(["Bob", "25", "Los Angeles"])
    writer.writerow(["Charlie", "35", "Chicago"])

# -----------------------------------------------
# 1. CSV Content Reader
# Write a Python program to read and display the content of a given CSV file. Use csv.reader
# -----------------------------------------------
print("🔹 1. CSV Content Reader")

with open(sample_csv_path, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print()

# -----------------------------------------------
# 2. CSV Line Counter
# Write a Python program to count the number of lines in a given CSV file. Use csv.reader
# -----------------------------------------------
print("🔹 2. CSV Line Counter")

with open(sample_csv_path, newline='') as file:
    reader = csv.reader(file)
    line_count = sum(1 for _ in reader)

print("Total lines:", line_count)
print()

# -----------------------------------------------
# 3. CSV String Parser
# Write a Python program to parse a given CSV string and get a list of lists of string values. Use csv.reader
# -----------------------------------------------
print("🔹 3. CSV String Parser")

csv_string = """Name,Age,City
Alice,30,New York
Bob,25,Los Angeles"""
reader = csv.reader(io.StringIO(csv_string))

parsed = list(reader)
print("Parsed CSV string:")
for row in parsed:
    print(row)

print()

# -----------------------------------------------
# 4. Current Line Reader from CSV
# Write a Python program to read the current line from a given CSV file. Use csv.reader
# -----------------------------------------------
print("🔹 4. Current Line Reader from CSV")

with open(sample_csv_path, newline='') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader, start=1):
        print(f"Line {i}: {row}")

print()

# -----------------------------------------------
# 5. CSV Header Skipper
# Write a Python program to skip the headers of a given CSV file. Use csv.reader
# -----------------------------------------------
print("🔹 5. CSV Header Skipper")

with open(sample_csv_path, newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    print("Header skipped:", headers)
    print("Remaining data:")
    for row in reader:
        print(row)

print()

# -----------------------------------------------
# 6. CSV Writer with Custom Delimiter
# Write a Python program to write and read a CSV file with a specified delimiter (e.g., `|`). Use csv.writer & csv.reader
# -----------------------------------------------
print("🔹 6. CSV Writer with Custom Delimiter")

custom_csv = "custom_delim.csv"
data = [
    ["ID", "Product", "Price"],
    [1, "Pen", 5.0],
    [2, "Notebook", 15.5]
]

# Write with delimiter |
with open(custom_csv, "w", newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(data)

# Read with delimiter |
with open(custom_csv, newline='') as file:
    reader = csv.reader(file, delimiter='|')
    print("Custom Delimiter Read:")
    for row in reader:
        print(row)

print()

# -----------------------------------------------
# 7. Write CSV from Dictionaries
# Write a Python program to write dictionaries and a list of dictionaries to a given CSV file. Use csv.DictWriter
# -----------------------------------------------
print("🔹 7. Write CSV from Dictionaries")

dict_csv = "dict_output.csv"
fieldnames = ['name', 'age', 'city']
rows = [
    {'name': 'Alice', 'age': 30, 'city': 'NYC'},
    {'name': 'Bob', 'age': 25, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

# Write dicts to CSV
with open(dict_csv, "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# Read and display it
with open(dict_csv, newline='') as file:
    reader = csv.reader(file)
    print("CSV from Dictionaries:")
    for row in reader:
        print(row)
