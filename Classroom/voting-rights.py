'''PROGRAM TO DETERMINE WHETHER IF A PERSON CAN VOTE OR NOT.'''

import os
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

resident = [] # LIST TO HOLD NAMES IF RESIDENCY IS TRUE.

while True:
    try:
        name = str(input("Enter your name: ")).strip().title()
        if len(name) == 0:
            print("Name cannot be empty. Please enter a valid name.\n")
            continue

        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.\n")
            continue
        elif age > 130:
            print("NEW WORLD RECORD FOR THE MOST LIVED PERSON CONGRATULATIONS!!!")

        resd = str(input("Are you currently a NZ resident? ('True' for yes, or 'False' for no): ")).upper()
        if resd == 'TRUE' or resd == 'FALSE': # BLOCKS ANY OTHER VARIABLE TYPED INPUT.
            break
        else:
            print("Please enter a valid input.\n")

    except ValueError: # BLOCKS ANY OTHER VARIABLE TYPED INPUT.
        print("Please enter a valid input.\n")


if resd == 'TRUE': # ADDS NAME TO THE RESIDENT LIST IF RESIDENT.
    resident.append(name)

else: # DOES NOTHING IF NOTHING ENTERED. 
    pass

if age >= 17 and name in resident: # CHECK IF PERSON MEETS THE CONDITIONS TO VOTE. 
    print("You can vote.")

else:
    print("You cannot vote.")
