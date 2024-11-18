'''
--- Simon Says ---
Created By: Lucas Lane
This program is designed to solve the Kattis problem "Simon Says". In this problem, the code has the user input a number that determines how many lines of input the code will
read, then the user inputs a series of commands. If the command doesnt start with the phrase "Simon says", there wont be an output for that line. However, if the phrase does
begin with "Simon says", then the code will output the rest of the phrase.
Steps:
1: Create a function that asks for an number input then repeats a loop of inputs for however many is equal to that number.
2: Create another function that reads those inputs and detects if they contain the phrase "Simon says". If they do, the function prints out the rest of the input. If the 
input doesnt contain the phrase, then the code outputs nothing.
'''

def Simonsays(simon):
    if "Simon says" in simon:
        length = int(len(simon))
        print(simon[11:length])



def test():
    assert(Simonsays("Simon says commit crime.") == "commit crime."), f'Expected: "commit crime.", but got: {Simonsays("Simon says commit crime.")}.'
    assert(Simonsays() == "")



loop = int(input())
i = 0

while i < loop:
    simon = input()
    Simonsays(simon)
    i += 1

