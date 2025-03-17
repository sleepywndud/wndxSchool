import os

if os.system == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

userinput = input("Enter a word: ")

for i in userinput:
    print(i)
