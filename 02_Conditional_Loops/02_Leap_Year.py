def check_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is a leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Example call
year = 2000
# year = int(input("Enter a year: "))
check_leap_year(year)

"""
 calculate the number of leap years between two given years (inclusive):

 def count_leap_years(start_year, end_year):
    leap_count = 0
    for year in range(start_year, end_year + 1):
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap_count += 1
    return leap_count

# Example usage
start = 2000
end = 2020
print(f"Number of leap years between {start} and {end}: {count_leap_years(start, end)}")

"""