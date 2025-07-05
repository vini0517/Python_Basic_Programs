# Sample Input: (Press Ctrl+C during input)
# Sample Output: Program interrupted by user.
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
