# getting first element of a list

def get_first_element(lst):
    """Return the first element of the list."""
    if lst:
        print(f"The first element of the list is: {lst[0]}")
    else:
        print("The list is empty.")

def get_lst():
    """Return the first element of the list."""
    lst = []
    element = input("Enter an element or press Enter to exit :")
    #element.append(lst)
    while element != "":
        lst.append(element)
        element = input("Enter an element or press Enter to exit :")
    return lst
def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == "__main__":
    main()
