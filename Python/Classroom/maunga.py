"""A Python program to help Otumoetai College to manage the number of students in each Maunga"""

########################################################################

import os

minimum = 1

karewa = []
manunui = []
maunganui = []
otanewainuku = []
puwhenua = []

listsorting = []

def menu():
    print("\nSelect your Maunga: \n "
    "\n 1. Karewa "
    "\n 2. Manunui "
    "\n 3. Maunganui "
    "\n 4. Otanewainuku "
    "\n 5. Puwhenua "
    "\n 6. Exit the program \n "
    )
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear()

########################################################################

while True: # LOOP FOR ASSIGNING STUDENTS TO MAUNGAS
    try:
        menu()
        maungainput = int(input("Enter the number of your Maunga: "))
        if 1 <= maungainput <= 5: # EXPECTED
            while True:  
                nameinput = input("Enter the student name: ").strip()
                if len(nameinput) > 0: # CHECKING FOR BLANK NAMES
                    break
                else:
                    print("Name cannot be blank. Please enter a valid name.")

            if maungainput == 1:
                karewa.append(nameinput)
            elif maungainput == 2: 
                manunui.append(nameinput)
            elif maungainput == 3:
                maunganui.append(nameinput)
            elif maungainput == 4: 
                otanewainuku.append(nameinput)
            elif maungainput == 5:
                puwhenua.append(nameinput)
            else: # THIS SHOULDN'T ACTIVATE IN ANY INSTANCE.
                print("Unexpected Error.")

        elif maungainput == 6:
            clear()
            print("Summary:\n")
            break

        else: # BOUNDARY EXCEPTION
            print("Maunga input must be an integer between 1~6.")

    except ValueError: # INVALID EXCEPTION
        print("Maunga input must be an integer between 1~6.")

########################################################################

karewacount = len(karewa)
manunuicount = len(manunui)
maunganuicount = len(maunganui)
otanewainukucount = len(otanewainuku)
puwhenuacount = len(puwhenua)

########################################################################

if karewacount >= minimum:
    print("Karewa:")
    for karewacount in karewa:
        print(karewacount)
    print("\n")
else:
    pass

########################################################################

if manunuicount >= minimum:
    print("Manunui:")
    for manunuicount in manunui:
        print(manunuicount)
    print("\n")
else:
    pass

########################################################################

if maunganuicount >= minimum:
    print("Maunganui:")
    for maunganuicount in maunganui:
        print(maunganuicount)
    print("\n")
else:
    pass

########################################################################

if otanewainukucount >= minimum:
    print("Otanewainuku:")
    for otanewainukucount in otanewainuku:
        print(otanewainukucount)
    print("\n")
else:
    pass

########################################################################

if puwhenuacount >= minimum:
    print("Puwhenua:")
    for puwhenuacount in puwhenua:
        print(puwhenuacount)
    print("\n")
else:
    pass

# HELP:
# MAUNGA WITH THE MOST AND LEAST PRINTING
