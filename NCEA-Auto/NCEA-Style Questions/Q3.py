import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

init = 200
remaining = [init] # LIST STARTING WITH 200
bankrupt = 0 

while True:
    try:
        spending = int(input("Enter the amount spent: "))
        if spending == bankrupt: # BREAKS WHEN INPUT == 0 
            break
        else:
            init -= spending # ASSIGNS NEW VALUE FOR {INIT}
            remaining.append(init)
            if init <= bankrupt: # BREAKS WHEN YOU HAVE NEGATIVE BALANCES
                break 

    except ValueError: # PREVENTS OTHER VARIABLE TYPES (STR, FLOAT, COMPLEX)
        print("That is not a valid transaction.")

print("My bank balances have been:")
for printing in remaining: # PRINTS MONEY HISTORY VERTICALLY
    print(printing)
