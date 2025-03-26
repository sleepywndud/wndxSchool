'''CodeRunner NCEA Style Questions - Question 3: Spending Tracker.'''

import os
os.system('clear')

init = 200
remaining = [init]
bankrupt = 0

while True:
    try:
        spending = int(input("Enter the amount spent:"))
        if spending == bankrupt: # BREAKS IF INPUT IS ZERO.
            break
        else:
            init =- spending
            remaining.append(init) # ADDS USERINPUT TO THE LIST IF DOESN'T MEET CONDITIONS.
            if init <= bankrupt: # BREAKS IF REMIANING IS ZERO.
                break

    except ValueError: # PREVENTS OTHER VARIABLE TYPES.
        print("That is not a valid transaction")

for wndud in remaining: # PRINTS SPENDING
    print(wndud)
