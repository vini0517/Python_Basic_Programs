#Change List Item
colors = input("Enter 3 colors: ").split()
new_color = input("Enter a new color to replace second one: ")
colors[1] = new_color

print("Updated list:", colors)

# Input: red green blue
# New color: yellow
# Output: ['red', 'yellow', 'blue']
