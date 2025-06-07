import os

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#########################

word = str(input("Give a word that starts with H: "))
checker = word.startswith(("H", "h")) #  True if H/h, False if not

while checker == True:
    print(f"Yes, {word} starts with H!")
    word = str(input("Give a word that starts with H: "))
    checker = word.startswith(("H", "h")) #  True if H/h, False if not

print(f"No, {word} doesn't start with H!")
