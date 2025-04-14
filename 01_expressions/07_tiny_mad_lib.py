"""
Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!


"""


STARTER_STRING: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective:str=(input("\033[1;3mPlease type an adjective and press enter.\033[0m\n"))
    
    noun:str=(input("\033[1;3mPlease type a noun and press enter.\033[0m\n"))
    
    verb:str=(input("\033[1;3mPlease type a verb and press enter.\033[0m\n"))
    print(STARTER_STRING + adjective + " " + noun + " " + verb) 

if __name__ == "__main__":
    main()