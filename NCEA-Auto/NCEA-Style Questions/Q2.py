import os

if os.system == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

temperatures = []
cold = 33
hot = 43
rightmin = 34
rightmax = 42
counter = 0

while True:
    try:
        userinput = float(input("Enter the temperature: "))
        if userinput == -1:
            break
        else:
            temperatures.append(userinput)

    except ValueError:
        print("Invalid temperature.")

for userinput in range(len(temperatures)):
    if temperatures[counter] <= cold:
        print("too cold")
        counter += 1
    elif temperatures[counter] >= hot:
        print("too hot")
        counter += 1
    elif temperatures[counter] >= rightmin and temperatures[counter] <= rightmax:
        print("just right")
        counter += 1

