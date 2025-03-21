import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

temperatures = []
cold = 33
hot = 43
rightmin = 34
rightmax = 42
byebye = -1
counter = 0

while True:
    try:
        userinput = float(input("Enter the temperature: "))
        if userinput == byebye: # IMMEDIATELY QUITS IF -1 (BYEBYE) ENTERED
            break
        else:
            temperatures.append(userinput)

    except ValueError: # RESTRICTS ANY OTHER INPUT THAN INT/FLOATS
        print("Invalid temperature.")

for userinput in range(len(temperatures)): # INDEXING THROUGH LIST AND PRINTING OUTPUT
    if temperatures[counter] <= cold:
        print("too cold")
        counter += 1
    elif temperatures[counter] >= hot:
        print("too hot")
        counter += 1
    elif temperatures[counter] >= rightmin and temperatures[counter] <= rightmax: # BETWEEN THE 'JUST RIGHT' TEMPERATURE CONDITION
        print("just right")
        counter += 1

