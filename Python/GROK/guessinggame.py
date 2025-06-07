
print("What is my favourite food?")
guess = str(input("Guess? ")).lower()

while guess != "electricity":
    print("Not even close.")
    guess = str(input("Guess? ")).lower()

print("You guessed it! Buzzzz")
