# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

def launch_spaceship():
    print("\nBe Ready Spaceship is about to launch.\n")  # Called once
    for i in range(10, 0, -1):
        print( i, end="  ") # Countdown from 10 to 1
        
        


    print("\nThe ship has lifted off!\n ")

if __name__ == "__main__": 
    launch_spaceship()