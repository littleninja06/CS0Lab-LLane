"""
Conditional Logic Lab
Updated By: Lucas Lane
CSCI 110 Lab
Date: 9/26/2024

Read and solve the Kattis problem: https://open.kattis.com/problems/twostones 

Algorithm Steps:
  1. Read the number of stones
  2. Check if the number of stones is odd or even
  3. Print the winner
    3.a. If the number is odd, Alice wins.
    3.b. Otherwise, Bob wins.
"""


def main():
    """Main function that solves the problem"""
    N = int(input()) #"How many stones are on the ground?"
    print(answer(N))
    # FIXME 1: read the number of stones #FIXED#
    # FIXME 2: call answer function passing the number of stones as an argument #FIXED#
    # FIXME 3: print the answer as shown in the sample output #FIXED#


def odd_even(number: int):
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even"""
    
    if (number % 2 == 0):
        return "even"
    else:
        return "odd"

    # FIXME 4: if the number divided by 2 has 0 remainder, return 'even' 
    # otherwise, return 'odd' #FIXED#


def answer(stone: int):

    evenorodd = odd_even(stone)
    if evenorodd == "odd":
        return "Alice"
    else:
        return "Bob"




if __name__ == "__main__":
    main()
