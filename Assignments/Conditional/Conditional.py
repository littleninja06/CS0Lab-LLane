'''
--- Conditionals ---
Created By: Lucas Lane
Much like the functions assignment, this assignment will take a series of inputed numbers and output the result of a math equation. This time, however, we will be doing it
with 5 given numbers, and we will be finding the sum, product, largest number, smallest number, and the average of the 5 given numbers.
Steps:
1 - Create a function for the addition of the 5 numbers.
2 - Create a function for the multiplication of the 5 numbers.
3 - Create a function that will detect the largest number of the 5 numbers and output it.
4 - Create a function that will detect the smallest number of the 5 numbers and output it.
5 - Create a function that will find the average of all 5 numbers.
6 - Create a main function that prompts the user to input 5 numbers, then use those inputed numbers in all the functions, returning the results.
7 - Create test functions to automatically test each function at least 2 times.
'''

def addition(a1, a2, a3, a4, a5):
    add = a1+a2+a3+a4+a5
    print("The sum is", add)
    return add

def multiplication(m1, m2, m3, m4, m5):
    product = m1*m2*m3*m4*m5
    print("The product is", product)
    return product

def greatest(l1, l2, l3, l4, l5):
    largest = l1
    if(largest < l2):
        largest = l2
    if(largest < l3):
        largest = l3
    if(largest < l4):
        largest = l4
    if(largest < l5):
        largest = l5
    print("The largest number is", largest)
    return largest

def least(s1, s2, s3, s4, s5):
    smallest = s1
    if(smallest > s2):
        smallest = s2
    if(smallest > s3):
        smallest = s3
    if(smallest > s4):
        smallest = s4
    if(smallest > s5):
        smallest = s5
    print("The smallest number is", smallest)
    return smallest

def average(av1, av2, av3, av4, av5):
    mean = addition(av1, av2, av3, av4, av5) / 5
    print("The average of the given numbers is", mean)
    return mean

def test():
    assert(addition(1,2,3,4,5) == 15)
    assert(addition(0,0,0,0,0) == 0)
    assert(multiplication(34,2,56,75,0) == 0)
    assert(multiplication(1,2,3,4,5) == 120)
    assert(greatest(1,2,3,4,5) == 5)
    assert(greatest(200,42,69,34,1) == 200)
    assert(least(1,2,3,4,5) == 1)
    assert(least(90,78,102,43,67) == 43)
    assert(average(1,2,3,4,5) == 3)
    assert(average(5,5,5,5,5) == 5)
    print("All tests passed!")

def main():

    test()

    num1 = int(input("Enter the first number. "))
    num2 = int(input("Enter the second number. "))
    num3 = int(input("Enter the third number. "))
    num4 = int(input("Enter the fourth number. "))
    num5 = int(input("Enter the fifth number. "))

    addition(num1, num2, num3, num4, num5)
    multiplication(num1, num2, num3, num4, num5)
    greatest(num1, num2, num3, num4, num5)
    least(num1, num2, num3, num4, num5)
    average(num1, num2, num3, num4, num5)

main()