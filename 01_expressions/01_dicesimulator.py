"""
Simulate rolling two dice, three times. Prints the results of each die roll. 
"""

import random

num_sides = 6
def roll_dice():
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)
    total = die1 + die2
    print("Total of two dice is: ", total)

def main():
    die1:int = 10
    print("Die 1 in main() starts as : ", str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Die 1 in main() is : ", str(die1))

if __name__ == "__main__":
    main()

