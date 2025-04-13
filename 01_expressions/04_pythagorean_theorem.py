"""
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
"""
from rich import print
import math
def pythagorean():
    print("[bold blue]Pythagorean Theorem Calculator[/bold blue]", end="\n\n")
    print("[bold italic]Enter the lengths of AB side of a right triangle.[/bold italic]\n\n", end="")
    side1 = input()
    side1 = float(side1)
    print("[bold italic]Enter the lengths of BC side of a right triangle.[/bold italic]\n\n", end="")
    side2 = input()
    side2 = float(side2)
    hypotenuse = math.sqrt(side1**2 + side2**2)
    print(f"[bold green]The length of the hypotenuse is: {hypotenuse:.2f}[/bold green]", end="\n\n")
    print("[bold red]Thank you for using the Pythagorean Theorem Calculator![/bold red]", end="\n\n")

    
    
# calling function

if __name__ == "__main__":
    pythagorean()
