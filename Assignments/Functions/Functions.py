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

def addition(a1, a2):
    added = a1 + a2
    print(a1, "+", a2 ,"=", added)
    return added

def multiplication(m1, m2):
    multiplied = m1 * m2
    print(m1, "X", m2, "=", multiplied)
    return multiplied

def division(d1, d2):
    divided = d1 / d2
    print(d1, "/", d2, "=", divided)
    return divided

def subtraction(s1, s2):
    subtracted = s1 - s2
    print(s1, "-", s2, "=", subtracted)
    return subtracted

def remainder(r1, r2):
    remain = r1 % r2
    print("The remainder of", r1, "/", r2, "is", remain)
    return remain

def exponentation(e1, e2):
    exponent = e1 ** e2
    print( e1, "to the power of", e2, "is", exponent)
    return exponent

def squareroot(sqrt):
    root = sqrt**.5
    print("The square root of", sqrt, "is", root)
    return root

def test():
    assert(addition(6, 3) == 9)
    assert(addition(1000, 342) == 1342)
    assert(multiplication(5, 6) == 30)
    assert(multiplication(1, 0) == 0)
    assert(division(0, 1) == 0)
    assert(division(1, 1000) == .001)
    assert(subtraction(1, 2) == -1)
    assert(subtraction(999, 999) == 0)
    assert(remainder(17, 5) == 2)
    assert(remainder(10, 2) == 0)
    assert(exponentation(3, 4) == 81)
    assert(exponentation(2, 0) == 1)
    assert(squareroot(4) == 2)
    assert(squareroot(1) == 1)
    print("All tests passed!")

test()

num1 = int(input("Select the first number for the operations."))
num2 = int(input("Select the second number for the operations."))
square = int(input("Pick a number to find the square root of."))

addition(num1, num2)
multiplication(num1, num2)
division(num1, num2)
subtraction(num1, num2)
remainder(num1, num2)
exponentation(num1, num2)
squareroot(square)
