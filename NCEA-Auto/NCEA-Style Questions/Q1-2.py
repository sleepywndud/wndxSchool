'''CodeRunner NCEA Style Questions - Question 1: Voltage of Batteries.'''

import os
os.system('clear')

batteries = [] # LIST TO HOLD ALL VOLTAGE INPUTS.
indexvar = 0 # VARIABLE TO INDEX THROUGH THE LIST.
minimumvalue = 0
goodbattery = 1.2

while True:
    try:
        userinput = float(input("Enter your input: "))
        if userinput < minimumvalue: # BREAKS IF INPUT IS BELOW ZERO. (EG: -1.)
            break
        else:
            batteries.append(userinput) # APPENDS TO THE BATTERIES LIST IF APPROPRIATE VALUE.

    except ValueError: # BLOCKS OTHER VARIABLE TYPES.
        print("Not robot compliant!")

for w in range(len(batteries)): # INDEXES THROUGH THE LIST TO PRINT BEEP/BOOP.
    if batteries[indexvar] >= goodbattery: # PRINTS BEEP IF BATTERY IS > 1.2.
        print("Beep")
        indexvar += 1
    else:
        print("Boop") # PRINTS BOOP IF BELOW 1.2.
        indexvar += 1
