"""
Lab - Playing with Loops
Updated By: Lucas Lane
CSCI 110
Date: 10-1-2024
Program prints geometric shapes of given height with * using loops
"""
import os
import sys

infinity = 2

def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of that height with *
    """
    i = 1
    while i <= height:
        print('*  '*i)
        i += 1
    print()  # print an empty line


def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    i = height
    while i > 0:
            print("*  "*i)
            i -= 1

    print()

    # FIXME3 ... #FIXED#
    pass


# FIXME4 #FIXED#
# Design and implement a function that takes a number as height and
# prints square of the given height with *.
# Square of height 5, e.g., would look like the following.
"""
*  *  *  *  *  
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
"""

def printSquare(height):
    i = 1
    while i <= height:
        print("* "*height)
        i += 1


def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # FIXME7 add a loop to make the program to continue to run until the user wants to quit #FIXED#
    # FIXME8 call clearScreen function to clear the screen for each round of the loop #FIXED#
    print('Program prints geometric shapes of given height with *')
    height = int(input('Please enter the height of the shape: '))
    clearScreen()
    # call printTriangle function passing user entered height
    printTriangle(height)

    # FIXME5 #FIXED#
    # Call printFlippedTriangle passing proper argument
    # Manually test the function
    printFlippedTriangle(height)

    # FIXME6 #FIXED#
    # Call the function defined in FIXME4 passing proper argument
    # Manually test the function

    printSquare(height)

    # FIXME9 #FIXED#
    # prompt user to enter y/Y to continue anything else to quit

    # FIXME10 #FIXED#
    # Use conditional statements to break the loop or continue in the loop


if __name__ == "__main__":
    Continue = "Y"
    while Continue == "Y" or Continue == "y":
        main()
        Continue = input("Would you like to countinue? Input Y or y for yes, anything else for no.")

