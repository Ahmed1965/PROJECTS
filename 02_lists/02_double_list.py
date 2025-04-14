"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:
"""

def double_list(numbers: list) -> list:
    """
    This function takes a list of numbers and returns a new list with each number doubled.
    """
    return [number * 2 for number in numbers]

def main():
    numbers: list = [1, 2, 3, 4, 5]
    print("The original list is: ", str(numbers))
    print("The new list is: ", str(double_list(numbers)))

if __name__ == "__main__":
    main()