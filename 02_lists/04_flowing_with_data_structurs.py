

def list_copy(numbers, data):
    """
    This function takes a list of numbers and data, and returns a new list with the data appended three times.
    """
    new_list = numbers[:]
    for i in range(3):
        new_list.append(data)
    return new_list
    
def main():
    message = input("Enter a message to copy: ")
    numbers = []
    print("Before " ,  numbers)
    numbers = list_copy(numbers, message)
    print("After " ,  numbers)
if __name__ == "__main__":
    main()