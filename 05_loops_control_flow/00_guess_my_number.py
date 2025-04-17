# Guess My Number

import random

secret_number = random.randint(1, 100)

def guess_a_number():




    while True:

        guess = int(input("Guess a number between 1 and 100: "))
        # print(secret_number)
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("You got it! The number is " + str(secret_number))
            break
if __name__ == "__main__":
    guess_a_number()