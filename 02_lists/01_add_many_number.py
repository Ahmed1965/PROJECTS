"""
Write a function that takes a list of numbers and returns the sum of those numbers.

"""

from typing import List

def sum_list_numbers(numbers: List[int])-> int:
    """
    This function takes a list of numbers and returns the sum of those numbers.
    """
    total: int = 0
    for number in numbers:
        total += number
    return total
def main():
    numbers: List[int] = [1, 2, 3, 4, 5]
    print("The sum of the numbers in the list is: ", str(sum_list_numbers(numbers)))    

if __name__ == "__main__":
    main()