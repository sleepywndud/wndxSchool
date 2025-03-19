import os

if os.system == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

voltage = []
counter = 0
while True:
    try:
        w = float(input("Enter your input: ")) 
        if w < 0: 
            break
        else:
            voltage.append(w)

    except ValueError: 
        print("Not robot compliant!")

for w in range(len(voltage)):
    if voltage[counter] >= 1.2:
        print("Beep")
        counter += 1

    elif voltage[counter] < 1.2:
        print("Boop")
        counter += 1
