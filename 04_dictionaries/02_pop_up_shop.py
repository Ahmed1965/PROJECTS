# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    fruit_dict = {"apple": 2.00, "banana": 2.50, "orange": 1.50}
    print("Welcome to the Fruit Shop!")

    # initialize variables for cost
    total_cost = 0

    # loop through dictionary and get user input
    for fruit, price in fruit_dict.items():
        qty = int(input(f"How many {fruit} do you want to buy? "))
        total_cost += qty * price

    print(f"You have ordered {qty} {fruit} for a total of ${total_cost:.2f}")

    print()
    print("Thank you for shopping with us!")

    # boiler plate code

if __name__ == "__main__":
        main()
        

                                                                                                                                                    