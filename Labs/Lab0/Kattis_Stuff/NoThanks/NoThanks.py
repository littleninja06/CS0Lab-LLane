'''
Author: Lucas Lane
Date: 10-16-2024
Program Info: Kattis problem - No Thanks - https://open.kattis.com/problems/nothanks
Algorithm Steps:
    Collect all numbers into a list
    Set score = 0
    Set first_value = first number in list
    for every next number:
        if incremented by 1 from previous number:
            don't change first_val
        else:
            add first_val to score
            set new first val to current number
    Profit
'''

def main():
    num_cards = int(input())
    numbers = input().split()
    numbers = list( map(int, numbers) )

    #print(numbers) # verify we get our numbers

    numbers.sort() # sort numbers list in ascending order
    #print(numbers)

    tot_score = numbers[0]
    first_score = numbers[0]
    previous = numbers[0]

    for i in range(1, num_cards):
        if(numbers[i] == previous+1):
            pass
            #tot_score += first_score
        else: # incremented by more than 1
            tot_score += numbers[i]
            #print("Current score = ", tot_score)
            #print("New first_score = ", first_score)

        previous = numbers[i]

    print(tot_score)

if __name__ == "__main__":
    main()