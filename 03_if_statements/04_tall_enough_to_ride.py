# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

MIN_HEIGHT = 9  # Minimum height in feet
from rich import print
def is_tall_enough(height: int) -> bool:
    """Check if a person is tall enough."""
    return height >= MIN_HEIGHT

def main():
    print("[bold italic]Enter your height in feet[/bold italic]")
    height = int(input())
    
    
    # Check if the user is tall enough
    if is_tall_enough(height):
        print(f"You are tall enough to ride!")
    else:
        print(f"You are not tall enough to ride.")

if __name__ == "__main__":
    main()