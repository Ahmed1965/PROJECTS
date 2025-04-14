# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# For example, the years 2000 and 2400 are leap years, but the years 1900 and 2100 are not leap years.

numb1: int = 4
numb2: int = 100
numb3: int = 400

def is_leap_year(year: int) -> bool:
    """Check if a given year is a leap year."""
    if year % numb1 == 0:
        if year % numb2 == 0:
            if year % numb3 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def main():
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
if __name__ == "__main__":
    main()