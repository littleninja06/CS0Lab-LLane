'''
--- A New Alphabet ---
This code is designed to solve the Kattis problem "A New Alphabet" by using a dictionary to redefine each letter in the alphabet. then, it takes an input and translates it to the new alphabet. If the input has a character that isnt in the dictionary, then it will output that character without translating it.
Steps:
1: Paste in the new alphabet.
2: Create a function for the input of the text.
3: Create a function that detects if a character is in the function, then translates that character.
4: If the character isnt in the alphabet, create an else for that situation that just outputs that character.
5: Run the function.
'''

newalpha = {
    'a':"@",
    'b':"8",
    'c':"(", 'd':"|)",
    'e':"3", 
    'f':"#", 
    'g':"6", 
    'h':"[-]", 
    'i':"|", 
    'j':"_|", 
    'k':"|<", 
    'l':"1", 
    'm':r"[]\/[]", 
    'n':r"[]\[]", 
    'o':"0", 
    'p':"|D", 
    'q':"(,)", 
    'r':"|Z", 
    's':"$", 
    't':"']['", 
    'u':"|_|", 
    'v':r"\/", 
    'w':r"\/\/", 
    'x':"}{", 
    'y':"`/", 
    'z':"2"
    }

def test():
    assert(phraseoutput("We are!") == r"\/\/3 @|Z3!")
    assert(phraseoutput("Great Scott!") == r"6|Z3@'][' $(0']['']['!")
    assert(phraseoutput("SuperCalaFragilisticExpialaDoucus") == r"$|_||D3|Z(@1@#|Z@6|1|$']['|(3}{|D|@1@|)0|_|(|_|$")
    print("All tests passed!")

def phraseoutput(phrase):
    phrase = phrase.lower()
    output = ""
    for i in range(len(phrase)):
        if phrase[i] in newalpha:
            output += newalpha[phrase[i]]
        else:
            output += phrase[i]
    return output

test()

text = input()

print(phraseoutput(text))