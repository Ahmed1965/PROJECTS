# Print 10 random numbers in the range 1 to 100.


import random

n:int=10
start:int=1
end:int=100

def print_random_numbers(n, start, end):
    for i in range(n):
        random_number = random.randint(start, end)
        print(random_number, end=", ")
    print()  # Print a newline after all numbers are printed

if __name__ == "__main__":
    print_random_numbers(n, start, end)