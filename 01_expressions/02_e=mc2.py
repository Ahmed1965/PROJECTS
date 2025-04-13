"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2
speed of light  is C = 299792458 m/s

8.987551787368176e+18 joules of energy per kilogram of mass.

"""
from rich import print


C = 299792458 # speed of light in m/s
E = 8.987551787368176e+18 # energy in joules per kg of mass

def mass_energy_equivalence():
    print("[bold italic]Enter mass in kg: [/bold italic] ", end="") 
    mass_in_kg = input()
    mass_in_kg = float(mass_in_kg)

    # Calculate energy using E = m * c^2
    mass_energy_equivalence = mass_in_kg * C**2
    print("[bold italic]The energy equivalent is: [/bold italic] ", end="") 
    print(str(mass_energy_equivalence), "Joules")
    
    # printing the result
    print("[bold italic] formula is E=mc^2[/bold italic]\n ",end="")
    print("[bold italic]The mass is[/bold italic] ",str(mass_in_kg),"kg")
    print("[bold italic]The speed of light is[/bold italic] ",str(C),"m/s")
    
    
    
       
    
    
    
    
    





if __name__ == "__main__":
    mass_energy_equivalence()