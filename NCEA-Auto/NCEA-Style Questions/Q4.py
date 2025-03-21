import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

minimum = 80  
maximum = 100
nerds = 0

grades = []

while True:
    user_input = input("Enter a score, or type 'done' to exit: ")
    if user_input.upper() == 'DONE': # BREAK IF INPUT == 'DONE'
        break
    try:
        grade = int(user_input)  # FLOATS TO INTEGER
        grades.append(grade)
    except ValueError: # BLOCKS OTHER VARIABLE TYPES (STR, COMPLEX)
        print("Invalid score!") 

for grade in grades:
    if minimum <= grade <= maximum:  # FILTER NETRDS
        nerds += 1

if nerds == 1:
    print(f"This class has {nerds} smart student!")
else:
    print(f"This class has {nerds} smart students!")
