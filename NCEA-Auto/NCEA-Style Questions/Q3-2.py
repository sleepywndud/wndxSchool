'''CodeRunner NCEA Style Questions - Question 3: Spending Tracker.'''

import os
os.system('clear')

init = 200
remaining = [init]
bankrupt = 0

while True:
    try:
        spending = int(input("Enter the amount spent:"))
        if spending == bankrupt:
            break
        else:
            init =- spending
            remaining.append(init)
            if init <= 0:
                break

    except ValueError: 
        print("That is not a valid transaction")

for wndud in remaining:
    print(wndud)
