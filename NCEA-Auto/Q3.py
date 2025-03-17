import os

if os.system == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

age = int(input("Enter your age: "))

if age != 1:
    print(f"You are {age} years old.")
elif age == 1:
    print(f"You are {age} year old.")
