#Python Program to Display Powers of 2 Using Anonymous Function

def display_powers_of_two(terms):
    result = list(map(lambda x: 2 ** x, range(terms)))
    print(f"The total terms are: {terms}")
    for i in range(terms):
        print(f"2 raised to power {i} is {result[i]}")

# Example usage
terms = 10
# terms = int(input("How many terms? "))
display_powers_of_two(terms)

