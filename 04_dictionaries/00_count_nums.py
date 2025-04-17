# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.


from rich import print

def count_numbers():
    """Counts the number of times each number appears in  a list."""
    numbers = []
    while True:
        print("[blue]Enter Number:[/blue]  ")
        user_input = input()
        # if user input is empty, break the loop
        if user_input == "":
            break
        try:
            user_input = int(user_input)
            numbers.append(user_input)
            
        except:     # check if the input is a number
            print("[red]Invalid input. Please enter a number.[/red]")
    return numbers

def create_count_dict(numbers):
    num_dict = {}
    for num in numbers:
        if num in num_dict:
            num_dict[num] +=1
        else:
            num_dict[num] = 1
    return num_dict
def print_num(num_dict):
    for num, count in num_dict.items():
        print(f"{num}[green]: count {count}: times[/green]")
def main():
    user_numbers = count_numbers()
    num_dict = create_count_dict(user_numbers)
    print_num(num_dict)

  
# Python boilerplate.
if __name__ == '__main__':
    main()



