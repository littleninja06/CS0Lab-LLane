"""
CSCI 110
List Lab

By: Lucas Lane
Date: 10-16-2024

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

import copy

totalInts = 10


def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        # FIXME0 add num into integers list #FIXED#
        i += 1
        intList.append(num)
        print(intList)
        pass
    return intList



def sortListInAscendingOrder(intList):
    intList.sort()


def sortListInDescendingOrder(intList):
    intList.sort(reverse = True)
    #FIXME3 (20 points) #FIXED#
    pass


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    printList(integers)
    truelist = copy.deepcopy(integers)
    print()
    # sort numbers
    sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    printList(integers)
    # FIXME4 (10 points)
    # Call sortListInDescendingOrder function #FIXED#
    sortListInDescendingOrder(integers)
    print("Numbers in descending order: ")
    printList(integers)
    # FIXME5 (10 points)
    # Print the sorted list in descending order #FIXED#
    # FIXME6 (10 points)
    # Print the largest number #FIXED#
    largestnumber = integers[0]
    print(largestnumber)
    # FIXME7 (10 points)
    # Print the smallest number #FIXED#
    smallestnumber = integers[9]
    print(smallestnumber)
    # FIXME8 (10 points) #FIXED#
    # Find and print the index of the smallest number
    print("The original list was: ", truelist)
    print(truelist.index(integers[9]))
    # FIXME9 (10 points) #FIXED#
    # Print the index of the largest number
    print(truelist.index(integers[0]))


# FIXME10 (20 points) #FIXED#
# Call main function if this file is run as the main module
print('call main() function to see partial outputs of the program...')

if __name__ == "__main__":
    main()