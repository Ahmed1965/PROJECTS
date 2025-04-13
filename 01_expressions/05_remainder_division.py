"""
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
"""

def remainder_division():

    # user dividend input 
    dividend = float(input("Enter the dividend: "))

    # user divisor input
    divisor = float(input("Enter the divisor: "))

    # calculate quotient and remainder
    quotient = dividend // divisor
    result = dividend % divisor
    print(f"The quotient is {quotient} and the remainder is {result}")



if __name__ == "__main__":
      remainder_division()