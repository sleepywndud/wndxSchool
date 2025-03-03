sentence = str(input("What did you say? ")).lower()

while sentence != "i love brussel sprouts!":
    uppercase = sentence.upper()
    print(uppercase)
    sentence = str(input("What did you say? ")).lower()
print("You're no fun!")
