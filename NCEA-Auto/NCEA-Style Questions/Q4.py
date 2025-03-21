import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

minimum = 80  
maximum = 100
nerds = 0

while True:
    user_input = input("Enter a score, or type 'done' to exit: ")
    if user_input.upper() == 'DONE': # BREAKS IF INPUT IS 'DONE'
        break
    try:
        grade = int(user_input) # INTS THE USER INPUT
        if minimum <= grade <= maximum: # CHECKING TO SEE IF IT MEETS NERDS
            nerds += 1
    except ValueError: # BLOCKS OTHER DATA TYPES (STR, COMPLEX)
        print("Invalid score!") 

if nerds == 1:
    print(f"This class has {nerds} smart student!")
else:
    print(f"This class has {nerds} smart students!")
