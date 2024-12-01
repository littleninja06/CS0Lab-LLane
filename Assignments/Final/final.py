'''
--- CS0 Final: Hangman ---
This final project is to make a hangman game.
'''

import pathlib
import random

print("Let's play hangman! Try and guess the word one letter at a time!")

my_path = pathlib.Path(__file__).parent.resolve()
readfile_name = f'{my_path}/words.txt'

with open(readfile_name, 'r') as my_file:
    line = "not empty"
    lines = []
    while( line != ""):
        line = my_file.readline().strip()
        if(line == ""):
            break
        lines.append(line)

chosen_word = random.choice(lines)
print(chosen_word)

def hangman(phrase):
    underscore = ""
    for i in range(len(phrase)):
        underscore += "_"
    print(underscore)

hangman(chosen_word)
