"""
Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.
"""

def calculate_ages():
    anton_age = 21
    beth_age = anton_age + 6            # 21 + 6 = 27
    chen_age = beth_age + 20            # 27 + 20 = 47
    drew_age = chen_age + anton_age     # 47 + 21 = 68
    ethan_age = chen_age                #  47

    # printing result

    print(f"Anton is {anton_age} years old\n")
    print(f"Beth is {beth_age} years old\n")
    print(f"Chen is {chen_age} years old\n")
    print(f"Drew is {drew_age} years old\n")
    print(f"Ethan is {ethan_age} years old\n")

# calling function
if __name__ == "__main__":
    calculate_ages()