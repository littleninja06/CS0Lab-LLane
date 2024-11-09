''' 
--- Guess The Number ---
Created By: Lucas Lane
This program will prompt the user to enter their name, then select a random number between 1 and 20, then it will prompt the user to try and guess that number within 
6 attempts, telling them if they guessed too high or too low on each guess. When the user does eventually guess the number, the program will inform the user how many tries it
took to get there, then ask if they would like to play again.
Steps:
1: Create a function to prompt the user to enter their name.
2: Create a function that selects a random number from 1 to 20 and define it as a variable.
3: Create a function that takes an input from the user and compares it to the randomly selected number, detecting if it is more or less than the random number.
4: If the guess is wrong, have the function loop, up to six times.
5: If the guess is correct, tell the user they got it, with how many tries it took. Then prompt them to enter either Y or N to do it again or to quit.
'''

import random

def main():
    name = input("Hello! Welcome to the guess the number game! What is your name? ")
    print("Hello, "+name+"! I am thinking of a number between 1 and 20. Try and Guess it!")
    number = random.randint(1,20)
    guess = int(input("Guess the number! "))
    tries = 0
    while tries < 6:
        if guess == number :
            tries += 1
            print("Congrats! you guessed the number in", tries, "attempts!")
            again = input("Would you like to go again? If so, type Y or y.")
            if again == "Y" or again == "y":
                main()
            else:
                print("Goodbye!")
                exit()
        else:
            tries += 1
            if guess > number:
                print("Your guess is too high.")
                guess = int(input("Guess again! "))
            if guess < number:
                print("Your guess is too low.")
                guess = int(input("Guess again! "))
    else:
        print("Unfortunate. You couldnt find the number in 6 guesses.")
        badagain = input("Would you like to try again? If so, type Y or y.")
        if badagain == "Y" or badagain == "y":
            main()
        else:
            print("Goodbye!")
            exit()

main()