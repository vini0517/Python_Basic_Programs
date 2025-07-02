animals = input("Enter animal names: ").split()
remove_item = input("Enter animal to remove: ")

animals.remove(remove_item)
print("After removal:", animals)

# Input: cat dog rabbit
# Remove: dog
# Output: ['cat', 'rabbit']
