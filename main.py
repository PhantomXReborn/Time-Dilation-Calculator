'''
Program: Time Dilation Calculator
Purpose: Compares proper time with coordinate time.
Language: Python
Author: Reece Hannah
'''

# Imports
import os
import math
import linecache
from time import sleep

# clear_screen Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    for i in range(5):
        for j in range(3):
            print(j*"*")
            sleep(0.1)
            clear_screen()

        clear_screen()  

# Menu Screen
def mainMenu():
    print("\n\tTime Dilation Calculator")
    print("\n\nMade by: Reece Hannah")

    print("\n\nWhat variable would you like to find? ")
    print("1. \'v\' Velocity")
    print("2. \'Δt\' Dilated time")
    print("3. \'Δt₀\' Proper time")
    choice = int(input(("---> ")))

    return choice
    
def calculator(choice):
    c = 3 * math.pow(10, 8) # Speed of light

    if choice == 1: # Finds velocity with proper and dilated time
        print("\n\tTime Dilation Calculator")
        print("\n\nMade by: Reece Hannah")

        proper = float(input("\n\nWhat is your Δt₀ (proper: sec):\n "))
        dilated = float(input("\n\nWhat is your Δt (dilated: sec):\n "))

        print("\n\nEquation:\n")
        print("v = c × √(1 − (Δt₀ / Δt)²)")
        
        velocity = math.sqrt(1 - (proper / dilated)**2)

        rounded_velocity = round(velocity, 2)

        print("\n\nVelocity: %.3f" % velocity + "c" + " ±%.3f" % (rounded_velocity-velocity) + "c")

    elif choice == 2: # Finds dilated time with velocity and proper time
        print("\n\tTime Dilation Calculator")
        print("\n\nMade by: Reece Hannah")

        velocity = float(input("\n\nWhat is your v (velocity: km/hr):\n "))
        proper = float(input("\n\nWhat is your Δt₀ (proper: sec):\n "))

        velocity = velocity/3600

        print("\n\nEquation:\n")
        print("Δt = Δt₀ / √(1 - v²/c²)")
        
        dilated = proper / (math.sqrt(1 - (velocity**2 / c**2)))

        rounded_dilated = round(dilated, 2)

        print("\n\Dilated time: %.3f" % dilated + "c" + " ±%.3f" % (rounded_dilated-dilated) + "sec")

    elif choice == 3: # Finds proper time with velocity and dilated time
        print("\n\tTime Dilation Calculator")
        print("\n\nMade by: Reece Hannah")

        velocity = float(input("\n\nWhat is your v (velocity: km/hr):\n "))
        dilated = float(input("\n\nWhat is your Δt (dilated: sec):\n "))

        velocity = velocity/3600

        print("\n\nEquation:\n")
        print("Δt₀ = Δt × √(1 - v²/c²)")
        
        proper = dilated * (math.sqrt(1 - (velocity**2 / c**2)))

        rounded_proper = round(proper, 2)

        print("\n\nProper time: %.3f" % proper + "c" + " ±%.3f" % (rounded_proper-proper) + "sec")

    else:
        print("Error")

match mainMenu():
    case 1:
        loading()
        calculator(1)
    case 2:
        loading()
        calculator(2)
    case 3:
        loading()
        calculator(3)
