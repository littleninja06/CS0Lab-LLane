#Math Operations

'''
Author: Lucas Lane
Date: 8/30/2024
Program: ASCII Art
Algorithm:
    Ask for user name
    Collect user name
    Greet user
    Use Variables to define 4 pieces of ASCII art
    print(art)
    
    Cite online sources for ASCII art if used
'''
minutes = 310

hours = minutes // 60
rem_minutes = minutes % 60
#stands for remaining minutes
#the "%" sign is what is splitting it up into rem_minutes per 60 minutes

print(str(hours) + " hours, and", str(rem_minutes) + " minutes.")
print(str(hours) + " hours, and " + str(rem_minutes) + " minutes.")
#redundant, but shows different ways to display a sentence with both "+" signs, or by using commas.

#Kattis Assignment

Anrarpark:  str = input("How many cars did Anrar park?")
Anrarpark = int(Anrarpark)
Hannespark:  str = input("How many cars did Hannes park?")
Hannespark = int(Hannespark)
ans = Anrarpark + Hannespark
print(ans)