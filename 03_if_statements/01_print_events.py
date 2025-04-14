# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do not write twenty print statements.

# The first 20 even numbers are 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, and 38.

def print_even_numbers(n):
    for i in range(n):
        print(i * 2, end=", ")

if __name__ == "__main__":
    print_even_numbers(20)