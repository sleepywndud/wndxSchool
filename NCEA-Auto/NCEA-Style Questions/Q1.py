import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

voltage = [] # LIST TO CONTAIN ALL VOLTAGE VALUES
counter = 0 # USED INSIDE FOR LOOP WHEN INDEXING
condition = 1.2

while True:
    try:
        winput = float(input("Enter your input: ")) 
        if winput < 0: # STOPS IF NEGATIVE NUMBERS INPUT
            break
        else: # REPEATS LOOP IF POSITIVE NUMBERS INPUT
            voltage.append(winput)

    except ValueError: # BLOCKS ANY VALUES THAT ISN'T INT/FLOAT
        print("Not robot compliant!")

for winput in range(len(voltage)): # LOOPS PRINTING BEEP/BOOP
    if voltage[counter] >= condition:
        print("Beep")
        counter += 1

    elif voltage[counter] < condition:
        print("Boop")
        counter += 1
