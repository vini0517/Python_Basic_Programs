from decimal import Decimal, getcontext, ROUND_UP, ROUND_DOWN, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_DOWN, ROUND_HALF_UP, ROUND_HALF_EVEN

# -----------------------------------------------
# 1. Decimal Construction
# Write a Python program to construct a Decimal from a float and a Decimal from a string.
# Also represent the decimal value as a tuple. Use decimal.Decimal
# -----------------------------------------------
print("🔹 1. Decimal Construction")

d1 = Decimal(0.1)
d2 = Decimal("0.1")
print("Decimal from float:", d1)
print("Decimal from string:", d2)
print("Tuple representation:", d2.as_tuple())

print()

# -----------------------------------------------
# 2. Rounding Up/Down Configuration
# Write a Python program to configure rounding to round up and round down a given decimal value.
# Use decimal.Decimal
# -----------------------------------------------
print("🔹 2. Rounding Up/Down")

val = Decimal("5.342")

getcontext().rounding = ROUND_UP
print("Rounded Up:", val.quantize(Decimal("0.1")))

getcontext().rounding = ROUND_DOWN
print("Rounded Down:", val.quantize(Decimal("0.1")))

print()

# -----------------------------------------------
# 3. Round to Nearest 0.10 (with 0.05 Exception)
# Write a Python program to round a decimal value to the nearest multiple of 0.10,
# unless already an exact multiple of 0.05.
# Use decimal.Decimal
# -----------------------------------------------
print("🔹 3. Round to Nearest 0.10 (with 0.05 exception)")

def custom_round(val):
    dec = Decimal(str(val))
    if (dec * 100) % 5 == 0 and (dec * 100) % 10 != 0:
        return dec
    return dec.quantize(Decimal("0.1"))

print("Input: 1.15 =>", custom_round(1.15))  # No rounding (exact multiple of 0.05)
print("Input: 1.16 =>", custom_round(1.16))  # Rounded to 1.2
print()

# -----------------------------------------------
# 4. Floor and Ceiling Rounding
# Write a Python program to configure the rounding to round to the floor, ceiling.
# Use decimal.ROUND_FLOOR, decimal.ROUND_CEILING
# -----------------------------------------------
print("🔹 4. Floor and Ceiling Rounding")

num = Decimal("-2.45")

getcontext().rounding = ROUND_FLOOR
print("Rounded Floor:", num.quantize(Decimal("0.1")))

getcontext().rounding = ROUND_CEILING
print("Rounded Ceiling:", num.quantize(Decimal("0.1")))

print()

# -----------------------------------------------
# 5. Rounding with Tie-Breaking Rules
# Write a Python program that can be configured to round to the nearest -
# with ties going towards 0 and ties going away from 0.
# Use decimal.ROUND_HALF_DOWN, decimal.ROUND_HALF_UP
# -----------------------------------------------
print("🔹 5. Rounding with Tie-Breaking Rules")

num1 = Decimal("2.25")
num2 = Decimal("-2.25")

getcontext().rounding = ROUND_HALF_DOWN
print("ROUND_HALF_DOWN (+2.25):", num1.quantize(Decimal("0.1")))
print("ROUND_HALF_DOWN (-2.25):", num2.quantize(Decimal("0.1")))

getcontext().rounding = ROUND_HALF_UP
print("ROUND_HALF_UP (+2.25):", num1.quantize(Decimal("0.1")))
print("ROUND_HALF_UP (-2.25):", num2.quantize(Decimal("0.1")))

print()

# -----------------------------------------------
# 6. Round to Nearest Even (Bankers' Rounding)
# Write a Python program to configure rounding to round to the nearest integer,
# with ties going to the nearest even integer. Use decimal.ROUND_HALF_EVEN
# -----------------------------------------------
print("🔹 6. Bankers' Rounding (ROUND_HALF_EVEN)")

getcontext().rounding = ROUND_HALF_EVEN
print("1.5 rounded:", Decimal("1.5").quantize(Decimal("1")))
print("2.5 rounded:", Decimal("2.5").quantize(Decimal("1")))

print()

# -----------------------------------------------
# 7. Scientific Notation Display
# Write a Python program to display a given decimal value in scientific notation.
# Use decimal.Decimal
# -----------------------------------------------
print("🔹 7. Scientific Notation Display")

value = Decimal("123456.789")
print("Scientific Notation:", "{:.2E}".format(value))

print()



"""
🔹 1. Decimal Construction
Decimal from float: 0.1000000000000000055511151231257827021181583404541015625
Decimal from string: 0.1
Tuple representation: DecimalTuple(sign=0, digits=(1,), exponent=-1)

🔹 2. Rounding Up/Down
Rounded Up: 5.4
Rounded Down: 5.3

🔹 3. Round to Nearest 0.10 (with 0.05 exception)
Input: 1.15 => 1.15
Input: 1.16 => 1.2

🔹 4. Floor and Ceiling Rounding
Rounded Floor: -2.5
Rounded Ceiling: -2.4

🔹 5. Rounding with Tie-Breaking Rules
ROUND_HALF_DOWN (+2.25): 2.2
ROUND_HALF_DOWN (-2.25): -2.2
ROUND_HALF_UP (+2.25): 2.3
ROUND_HALF_UP (-2.25): -2.3

🔹 6. Bankers' Rounding (ROUND_HALF_EVEN)
1.5 rounded: 2
2.5 rounded: 2

🔹 7. Scientific Notation Display
Scientific Notation: 1.23E+05

"""