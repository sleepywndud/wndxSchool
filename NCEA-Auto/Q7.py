import os

if os.system == "nt":
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

print(f"No, {word} does not start with H!")
