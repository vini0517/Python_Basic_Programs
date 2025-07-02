colors = input("Enter colors: ").split()
item = input("Enter item to insert: ")
pos = int(input("Enter position (0-based index): "))

colors.insert(pos, item)
print("After insert:", colors)

# Input: red green
# Insert: yellow
# Position: 1
# Output: ['red', 'yellow', 'green']
