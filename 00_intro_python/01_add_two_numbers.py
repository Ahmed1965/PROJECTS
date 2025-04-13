# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:


# creating a function which takes two integer inputs from the user and calculates their sum

def main():
    """
    This function takes two integer inputs and returns their sum
    """

    numb1 = input("Enter first number:")
    # converting input into integer
    numb1 = int(numb1)
    print(numb1)

    numb2 = input("Enter second number:")

    # converting input into integer
    numb2 = int(numb2)
    # calculating the sum of two numbers

    sum = numb1 + numb2
    # printing the sum of two numbers

    print(f"The sum of {numb1} and {numb2} is {sum}")

# calling the function
if __name__ == "__main__":
    main()
