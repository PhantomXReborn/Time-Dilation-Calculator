'''
Program: Time Dilation Calculator
Purpose: Compares proper time with coordinate time.
Language: Python
Author: Reece Hannah
'''

# Imports
import os
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

    print("\n\nChoose a difficulty range for your program: ")
    print("1. BEGINNER PROJECTS")
    print("2. INTERMEDIATE PROJECTS")
    print("3. ADVANCED PROJECTS")
    choice = int(input(("---> ")))

    if not input("Press ENTER to generate an idea (or type anything to exit): "):
        return choice
    else:
        print("Exiting program.")