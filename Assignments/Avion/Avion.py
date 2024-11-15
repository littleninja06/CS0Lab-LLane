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



def findfbi(b1, b2, b3, b4, b5):

    allblimps = b1 + b2 + b3 + b4 + b5

    if "FBI" in allblimps:
        lines = ""
        if "FBI" in b1:
            lines += "1 "
        if "FBI" in b2:
            lines += "2 "
        if "FBI" in b3:
            lines += "3 "
        if "FBI" in b4:
            lines += "4 "
        if "FBI" in b5:
            lines += "5 "
        print(lines)
        return lines
    else:
        print("HE GOT AWAY!")
        return "HE GOT AWAY!"

def test():
    
    assert(findfbi("ASFB-UI", "FBI-78", "CI-A-U21", "COMFBI", "GR-E-E7") == "2 4 "), f"Expected: 2 4 , But got {findfbi("ASFB-UI", "FBI-78", "CI-A-U21", "COMFBI", "GR-E-E7")}"
    assert(findfbi("Greatscott", "A", "FBI", "CFIRS-FBI", "FEBI") == "3 4 "), f"Expected: 3 4 5 , But got {findfbi("Greatscott", "A", "FBI", "CFIRS-FBI", "FEBI")}"
    assert(findfbi("SANJI", "USOPP", "ZORO", "LUFFY", "NAMI") == "HE GOT AWAY!"), f"Expected: HE GOT AWAY!, But got {findfbi("SANJI", "USOPP", "ZORO", "LUFFY", "NAMI")}"
    return print("All tests passed!")

test()

b1 = input()
b2 = input()
b3 = input()
b4 = input()
b5 = input()
    
findfbi(b1, b2, b3, b4, b5)



