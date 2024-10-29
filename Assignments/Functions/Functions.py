'''
--- A Basic Calculator Using Functions And Automated Unit Testing ---
Created By: Lucas Lane
This program is a rudamentary calculator that has a series of functions that take 2 input numbers and output their sum, product, quotient, difference, 
remainder of their division, and the first to the power of the second. Also, include a function that takes the square root of a number.
Steps:
1 - Create a function for the addition of two numbers.
2 - Create a function for the multiplication of two numbers.
3 - Create a function for the division of two numbers.
4 - Create a function for the subtraction of two numbers.
5 - Create a function for finding the remainder of two numbers.
6 - Create a function for the exponentation of two numbers.
7 - Create a function to find the square root of a number. (Inputed in the function)
8 - Create inputs for the two numbers
9 - Call all of the functions
10 - Create test cases, 7 of them.
'''

def addition():
    added = num1 + num2
    print(num1,"+", num2 ,"=", added)

def multiplication():
    multiplied = num1 * num2
    print(num1, "X", num2, "=", multiplied)

def division():
    divided = num1 / num2
    print(num1, "/", num2, "=", divided)

def subtraction():
    subtracted = num1 - num2
    print(num1, "-", num2, "=", subtracted)

num1 = int(input("Select the first number for the opperations."))
num2 = int(input("Select the second number for the opperations."))

addition()
multiplication()
division()