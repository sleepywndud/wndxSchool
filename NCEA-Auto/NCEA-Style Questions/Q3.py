import os

if os.system == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

init = 200
remaining = [init]
bankrupt = 0

while True:
    try:
        spending = int(input("Enter the amount spent: "))
        if spending == bankrupt:
            break
        else:
            init -= spending
            remaining.append(init)
            if init <= bankrupt:
                break

    except ValueError:
        print("That is not a valid transaction.")

print("My bank balances have been:")
for printing in remaining:
    print(printing)
