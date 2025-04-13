# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# importing library to decorate user input
from rich import print

def animal():
    animal = input("What is your favorite animal? ")
    # inserting space
    print("\n\n")
    # converting user input into bold and italic
    print(f"[bold italic] My favorite animal is also {animal}![bold italic]")
# calling the function
if __name__ == "__main__":
    animal()