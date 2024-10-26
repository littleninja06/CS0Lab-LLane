'''
--- Triangle Assignment ---
Created By: Lucas Lane
CSCI 110
Date: 10-25-2024
This program will find both the area and the perimiter of a triangle based on the length of it's sides.
Steps:
1 - Create 3 inputs for each side and assign them to variables
2 - Add together the 3 inputs and define them as the perimiter, printing it out.
3 - Use Heron's Formula to find the area of the triangle based off the perimiter of the triangle.
4 - Put in necessary print statements to make it clear what is happening in the code.
Bonus Step: Find a way see if the 3 given side lengths can actually form a triangle.
'''

print("Welcome! This code will take the length's of 3 sides of a triangle that you put in, and output the perimiter and area of the triangle!")

a = (input("Input the first side's length."))
b = (input("Input the second side's length."))
c = (input("Input the third side's length."))
sidea = int(a)
sideb = int(b)
sidec = int(c)
perimeter = sidea + sideb + sidec
strperimeter = str(perimeter)
ar = ((perimeter)*(perimeter - sidea)*(perimeter - sideb)*(perimeter - sidec))**.5
area = str(ar)

print("The sides given are "+ a +", " + b + ", and " +c+ ".")
print("The perimiter of the triangle is equal to " +strperimeter+ ".")
print("The area of the triangle is equal to "+area+".")