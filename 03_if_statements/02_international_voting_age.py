# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries. Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, AGE = 16,  Stanlau, AGE=25,   and Mayengua, AGE = 48 the voting ages are very different:

from rich import print

PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def can_vote_in_country(age, country_age):
    """Check if a person can vote in a given country based on their age."""
    return age >= country_age
def main():
    # ask user for his age
    age = int(input("Enter your age: "))
    # ask user for his country
    print("\nSelect a country to check if you are eligible to vote : ")
    print("[1] Peturksbouipo")
    print("[2] Stanlau")
    print("[3] Mayengua")
    choice = input("Enter the number of corresponding to the country: ")
    if choice == "1":
            if can_vote_in_country(age, PETURKSBOUIPO_AGE):
                print("[blue]You can vote in Peturksbouipo.[/blue]")
            else:
                print("[red]You cannot vote in Peturksbouipo.[/red]")
    elif choice == "2":
                if can_vote_in_country(age, STANLAU_AGE):
                    print("[blue]You can vote in Stanlau.[/blue]")
                else:
                    print("[red]You cannot vote in Stanlau.[/red]")
    elif choice == "3":
                if can_vote_in_country(age, MAYENGUA_AGE):
                    print("[blue]You can vote in Mayengua.[/blue]")
                else:
                    print("[red]You cannot vote in Mayengua.[/red]")
    else:
        print("[red]Invalid choice. Please select a valid country.[/red]")


if __name__ == "__main__":
    main()