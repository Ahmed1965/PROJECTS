# Get last Element of a List


def get_last_element():
    """Return the last element of the list."""
    lst = []
    element = input("Enter an element or press Enter to exit :")
    while element != "":
        lst.append(element)
        element = input("Enter an element or press Enter to exit :")
    if lst:
            print(f"The last element of the list is: {lst[-1]}")
    else:
            print("The list is empty.") 
    

if __name__ == "__main__":
    get_last_element()
