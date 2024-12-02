'''
--- CS0 Final: Hangman ---
This final project is to make a hangman game.
Steps:
1: Make the code.
2: Profit.
'''

import pathlib
import random
import copy

def fail0():
    print("______________")
    print("|        |   ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|____________")

def fail1():
    print("______________")
    print("|       _|_ ")
    print("|      /   \ ")
    print("|      \___/ ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|____________")

def fail2():
    print("______________")
    print("|       _|_ ")
    print("|      /   \ ")
    print("|      \___/ ")
    print("|        |    ")
    print("|        |    ")
    print("|        |    ")
    print("|            ")
    print("|            ")
    print("|            ")
    print("|____________")

def fail3():
    print("______________")
    print("|       _|_ ")
    print("|      /   \ ")
    print("|      \___/ ")
    print("|        |    ")
    print("|        |    ")
    print("|        |    ")
    print("|       /    ")
    print("|      /      ")
    print("|            ")
    print("|____________")

def fail4():
    print("______________")
    print("|       _|_ ")
    print("|      /   \ ")
    print("|      \___/ ")
    print("|        |    ")
    print("|        |    ")
    print("|        |    ")
    print("|       / \   ")
    print("|      /   \  ")
    print("|            ")
    print("|____________")

def fail5():
    print("______________")
    print("|       _|_ ")
    print("|      /   \ ")
    print("|   \  \___/ ")
    print("|    \___|    ")
    print("|        |    ")
    print("|        |    ")
    print("|       / \   ")
    print("|      /   \  ")
    print("|            ")
    print("|____________")

def fail6():
    print("______________")
    print("|       _|_ ")
    print("|      /   \ ")
    print("|   \  \___/  / ")
    print("|    \___|___/    ")
    print("|        |    ")
    print("|        |    ")
    print("|       / \   ")
    print("|      /   \  ")
    print("|            ")
    print("|____________")

print("Let's play hangman! Try and guess the word one letter at a time!")

my_path = pathlib.Path(__file__).parent.resolve()
readfile_name = f'{my_path}/words.txt'

with open(readfile_name, 'r') as my_file:
    lines = my_file.readlines()

lines = [line.strip() for line in lines]

def pickrandom():
    chosen_word = random.choice(lines).lower()
    global answer
    answer = copy.deepcopy(chosen_word)
    chosen_word = list(chosen_word)
    return chosen_word

def hangman(phrase):
    progress = 0
    attempt = 0
    underscore = []
    one = 0
    new_underscore = []
    while one < len(phrase):
        new_underscore += ["_"]
        underscore += ["_"]
        one += 1
    length = len(phrase)
    test = underscore
    print("".join(test))
    while attempt < 6:
        guess = input("Guess a letter!").lower()
        if len(guess) > 1:
            print("Your guess has to be one character, try again!")
            guess = input("Guess a letter!").lower()
        runs = 0
        while runs < length:
            if new_underscore[runs - 1] == phrase[runs - 1]:
                new_underscore[runs - 1] = phrase[runs - 1]
                runs += 1
            if new_underscore[runs - 1] != phrase[runs - 1]:
                if guess in phrase[runs - 1]:
                    new_underscore[runs - 1] = guess
                    runs += 1
                else:
                    new_underscore[runs - 1] = "_"
                    runs += 1
        runs = 0
        if new_underscore == phrase:
            if attempt == 0:
                fail0()
            if attempt == 1:
                fail1()
            if attempt == 2:
                fail2()
            if attempt == 3:
                fail3()
            if attempt == 4:
                fail4()
            if attempt == 5:
                fail5()
            progress += 1
            print("congratulations! You guessed the word in", progress, "tries!")
            shown = "".join(new_underscore)
            print(shown)
            attempt = 7
        if new_underscore != phrase:
            if test == new_underscore:
                attempt += 1
                if attempt == 0:
                    fail0()
                if attempt == 1:
                    fail1()
                if attempt == 2:
                    fail2()
                if attempt == 3:
                    fail3()
                if attempt == 4:
                    fail4()
                if attempt == 5:
                    fail5()
                print("There are no "+guess+"'s, try again!")
                progress += 1
                shown = "".join(new_underscore)
                print(shown)
            else:
                if attempt == 0:
                    fail0()
                if attempt == 1:
                    fail1()
                if attempt == 2:
                    fail2()
                if attempt == 3:
                    fail3()
                if attempt == 4:
                    fail4()
                if attempt == 5:
                    fail5()
                print(guess+" is in the word!")
                progress += 1
                test = copy.deepcopy(new_underscore)
                shown = "".join(new_underscore)
                print(shown)
    if attempt == 6:
        fail6()
        print("You failed! The word was "+answer+".")

Continue = "Y"
while Continue == "Y" or Continue == "y":
    pickrandom()
    hangman(pickrandom())
    Continue = input("Would you like to countinue? Input Y or y for yes, anything else for no.")