minimum = 12
password = input("Password to check: ")

if 'password' in password:
    print("You shouldn't use a password in a password!")
    password = "90penguinRacers"
    print(f"Here's a suggestion for a passphrase: {password}")

elif len(password) < minimum:
    print("Too short!")

else:
    print("That's an OK password.")
