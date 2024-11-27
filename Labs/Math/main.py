"""
Math and Variables Lab
By: Lucas Lane
CSCI 110 Lab
Date: 9/3/2024
 
Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""

import sys


def main():
    """Main function that solves the problem
    """

    # FIXME1 - read input data into a variable #fixed#
    line = input()
    # split the data into two numbers
    a, b = line.split()
    # check to see if the data is split correctly
    a = int(a)
    b = int(b)
    ans = a + b
    print(ans)
    # FIXME 2: convert string a into integer #fixed#
    # FIXME 3: convert string b into integer #fixed#
    # FIXME 4: add two numbers and store the result into ans variable #fixed#
    # FIXME 5: print the answer as shown in the sample output #fixed#


main()  # call main function
