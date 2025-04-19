# Write a program to print terms in the Fibonacci sequence up to a maximum value.


max_value_fib: int = 1000


def main(n):
    a, b  = 0,1
    for _ in range(n):
        a,b = b, a + b
        print(a)


if __name__ == "__main__":
    main(10)