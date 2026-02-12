"""
print_large-number.py
This program writes out extremely large numbers in their entirety to a specified file.

Careful: It removes the global limit for converting between int and str!
This safeguard has been implemented to mitigate the risk of DoS-attacks (CVE 2020-10735).
https://docs.python.org/3/library/stdtypes.html#integer-string-conversion-length-limitation

Author: Lukas Brinias (https://github.com/lukasbrinias)
"""
import sys
sys.set_int_max_str_digits(0)

# Initialize variables
coefficient: int = 0
exponent: int = 0
number: int = 0

# Get user input for the coefficient
while True:
    try:
        coefficient = int(input("Coefficient: "))
        if coefficient > 0:
            break
    except ValueError:
        pass
    print("Try again.")

# Get user input for the exponent
while True:
    try:
        exponent = int(input("Exponent: "))
        if exponent > 0:
            break
    except ValueError:
        pass
    print("Try again.")

# Compute
number: int = coefficient * (1 << exponent)

# Write to file with SI digit grouping (U+202F)
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"{number:_}".replace("_", "\u202f"))

# Confirm 
print(f"Wrote {len(str(number))} digits to file.")
