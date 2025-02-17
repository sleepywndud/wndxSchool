
# Take 15 user inputs into a list, and print out the number of odd and even numbers.

import os

def clear(): # FUNCTION TO CLEAR CLI BEFORE RUNNING PROGRAM
    if os.name == 'nt': os.system('CLS')
    else: os.system('CLEAR')
clear() # CLEARS CLI BEFORE RUNNING

list = [] # EMPTY LIST TO TAKE IN USER INPUTS
counter = 0 # COUNTER VARIABLE FOR ODD/EVEN NUMBER CHECKER
odd = 0
even = 0

for k in range(15): # ASKS THE USER 15 TIMES
    userinput = int(input("Number: "))

    list.append(userinput) # PUTS USER INPUT INTO A LIST

for i in range(15): # ODD/EVEN NUMBER CHECKER
    if list[counter] % 2 == 1: # ODD
        odd += 1
    else: # EVEN
        even += 1

    counter += 1 # NEXT NUMBER IN LIST

print(f"There are {odd} odd numbers, and {even} even numbers in your input.")
