'''
--- Lists: Falling Apart ---
This assignment for the Kattis problem "Falling Apart" will ask for an input of one integer that will determine the amount of inputs on the next line. On said next
line, the user inputs that amount of integers. Those integers will then be sorted in descending order, then added together into two sets in an alternating series.
The code will then output the values of those two series.
Steps:
1: Create a main function.
2: Create an input to determine the number of inputs later. Input must be between 1 and 15.
3: Create another input function based off the previous input function to input an amount of integers equal to the previous input.
4: Sort the second set of inputs in descending order.
5: Create a function to seperate the list of inputs into two sets, seperated by an odd or even position in the list.
6: Add together the two new sets, and output them.
REMEMBER TO FORMAT FUNCTIONS TO BE ABLE TO BE TESTED BY ASSERT FUNCTIONS
'''

def main():

    amount = int(input())

    if 1 <= amount <= 15:
        numlist = []
        nums = input()
        nums = nums.split(" ", amount)
        numlist = list(nums)
        numlist.sort(reverse=True)
        Bob = 0
        Alice = 0
        runs = 1
        while runs <= amount:
            for i in numlist:
                i = int(i)
                if 1 <= i <= 100:
                    if runs % 2 == 0:
                        Bob = Bob + i
                        runs += 1
                    else:
                        Alice = Alice + i
                        runs += 1
        print(Alice, Bob)

main()