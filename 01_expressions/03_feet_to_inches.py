"""Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural."""

# Constant

FEET_TO_INCHES = 12

def feet_to_inches():
    feet = float(input("Enter Feet: \n"))

    inches = feet * FEET_TO_INCHES
    print(f"{feet} feet is equal to {inches} inches\n")

# calling function
feet_to_inches()