import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

userinput = input("Enter a card: ")

while userinput in cards:
    print("That's a playing card!")
    userinput = input("Enter a card: ")

print("That's not a playing card!")
