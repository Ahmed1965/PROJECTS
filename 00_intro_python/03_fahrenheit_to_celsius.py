# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def temperature():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    # converting celsius to fahrenheit
    celsius = (fahrenheit - 32) * 5 / 9

    # printing the result
    print(f"The temperature {fahrenheit}"+ chr(176) + "F"+""+ f" is in Celsius : {celsius:.2f}" + chr(176) + "C")

    # calling function
if __name__ == "__main__":
    temperature()
