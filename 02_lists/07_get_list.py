# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.


from rich import print

def get_list():
    my_lst = []
    while True:
        element = input("Enter a list Element:  ")
        if element == "":
            break
        my_lst.append(element)
        print(f"[blue]{element}[/blue] added to list successfully")
    print("\n[bold blue] Final List: [/bold blue] ", my_lst)

if __name__ == "__main__":
    get_list()