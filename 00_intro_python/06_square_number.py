"""
Ask the user for a number and print its square.
"""


def square_number():
    # Prompt the user for a number
    number = float(input("Enter a number: "))

    # Calculate the square of the number
    square = number * number

    # Print the result
    print(f"The square of {number} is {square}")

if __name__ == "__main__":
    square_number()