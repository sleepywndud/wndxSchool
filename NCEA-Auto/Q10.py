import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

numbers = []
userinput = input("Enter a number: ")

while userinput != "quit":
    integerchecker = int(userinput)

    if integerchecker % 2 == 1: # ODD CONDITION
        numbers.append(userinput)
        userinput = input("Enter a number: ")

    elif integerchecker % 2 == 0: # EVEN CONDITION
        userinput = input("Enter a number: ")

for i in numbers:
    print(i)
