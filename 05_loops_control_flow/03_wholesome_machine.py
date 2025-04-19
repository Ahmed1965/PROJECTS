# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.")

AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type following affirmation : " + AFFIRMATION)

    user_feed_back = input() # get user feed back

    while user_feed_back != AFFIRMATION:  # user feed back is not equal to affirmation
        print("Please type the correct affirmation.  : " + AFFIRMATION)
        user_feed_back = input()

    print("You write the correct affirmation.")

if __name__ == "__main__":
    main()