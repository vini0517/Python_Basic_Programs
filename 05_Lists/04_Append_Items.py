#Append Item

cities = input("Enter cities: ").split()
new_city = input("Enter a city to append: ")
cities.append(new_city)

print("After append:", cities)

# Input: Delhi Mumbai
# New city: Chennai
# Output: ['Delhi', 'Mumbai', 'Chennai']
