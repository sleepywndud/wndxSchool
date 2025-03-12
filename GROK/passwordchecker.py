import os 
os.system('clear')

minimum = 12
password = input("Password to check: ")

if 'password' in password:
    print("You shouldn't use 'password' in a password!")
    newpassword = password.replace("password", "my90penguinRacers")
    print(f"Here's a suggestion for a passphrase: {newpassword}")

elif len(password) < minimum:
    print("Too short!")

else:
    print("That's an OK password.")
