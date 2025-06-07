'''CodeRunner NCEA Style Questions - Question 2: Ideal Temperatures.'''

import os
os.system('clear')

temperatures = []
cold = 33
hot = 43
rightmin = 34
rightmax = 42
byebye = -1
indexvar = 0

while True:
    try:
        userinput = float(input("Enter the temperature: "))
        if userinput == byebye: # IMMEDIATELY QUITS IF -1 (BYEBYE) ENTERED.
            break
        else: # APPENDS USERINPUT TO THE LIST IF APPROPRIATE VARIABLE TYPE ENTERED.
            temperatures.append(userinput)

    except ValueError: # RESTRICTS ANY OTHER INPUT THAN INT/FLOATS.
        print("Invalid temperature.")

for userinput in range(len(temperatures)): # INDEXING THROUGH LIST AND PRINTING OUTPUT DEPENDING ON CONDITION.
    if temperatures[indexvar] <= cold:
        print("too cold")
        indexvar += 1
    elif temperatures[indexvar] >= hot:
        print("too hot")
        indexvar += 1
    elif temperatures[indexvar] >= rightmin and temperatures[indexvar] <= rightmax: # BETWEEN THE 'JUST RIGHT' TEMPERATURE CONDITION.
        print("just right")
        indexvar += 1
