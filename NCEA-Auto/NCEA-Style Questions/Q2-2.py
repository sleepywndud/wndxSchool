'''CodeRunner NCEA Style Questions - Question 2: Ideal Temperatures.'''

import os
os.system('clear')

temperatures = [] # TEMPERATURES TO HOLD ALL USERINPUTS.
indexvar = 0 # VARIABLE FOR INDEXING THROUGH THE LIST. 

right_min = 34
right_max = 42

byebye = -1 # QUIT CONDITION VARIABLE.

while True:
    try:
        userinput = float(input("Enter the temperature: "))
        if userinput == byebye: # IF USERINPUT IS -1, QUITS THE PROGRAM.
            break
        else: # APPENDS USERINPUT TO THE TEMPERATURES LIST IF APPROPRIATE VARIABLE TYPE.
            temperatures.append(userinput)

    except ValueError: # BLOCKS OTHER VARIABLE TYPES, (EG: STRING, COMPLEX, ETC..)
        print("Invalid temperature.")

for indexer in range(len(temperatures)): # PRINTS OUTPUT ACCORDINGLY DEPENDING ON CONDITIONS.
    if temperatures[indexvar] < right_min:
        print("too cold")
    elif temperatures[indexvar] > right_max:
        print("too hot")
    else:
        print("just right")
