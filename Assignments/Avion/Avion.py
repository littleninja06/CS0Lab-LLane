'''
--- Avion ---
This program aims to identify whether a set of codes for blimps from an input contains the set of letters "FBI". If the codes dont contain FBI anywhere, it will
output "He got away!". If it does contain FBI, it should output which numbered rows contain that string of characters. There should be 5 rows of inputs for the codes,
with each row containing an upwards of 11 characters of the english alphabet, a dash, and the numbers 0 through 9.
Steps:
1: Create code for the input of the 5 codes.
2: Create a function to detect whether or not any of the codes contain the string "FBI".
3: Make code such that if any of the codes do contain the string "FBI", then the code detects and outputs which lines the string is in.
4: Make code such that if it can't find the string "FBI", it outputs "HE GOT AWAY!".
5: Create 3 test functions to ensure that the code is working properly.
6: Ensure that any input functions dont have any text in them such that the code is compatible with Kattis.
'''

blimp1 = input()
blimp2 = input()
blimp3 = input()
blimp4 = input()
blimp5 = input()

def findfbi():
    r1 = ""
    r2 = ""
    r3 = ""
    r4 = ""
    r5 = ""
    if "FBI" in blimp1:
        r1 == 1
    if "FBI" in blimp2:
        r2 == 2
    if "FBI" in blimp3:
        r3 == 3
    if "FBI" in blimp4:
        r4 == 4
    if "FBI" in blimp5:
        r5 ==5
    else:
        print("HE GOT AWAY!")
    
    print(r1,r2,r3,r4,r5)

findfbi()
