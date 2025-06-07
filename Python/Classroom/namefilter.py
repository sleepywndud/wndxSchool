import os


def clear():
    if os.name == "nt":
        os.system("CLS")
    else:
        os.system("CLEAR")


clear()

all_name_list = []
user_input = input("Enter a name: ").title()


while user_input != "":
    name_list = list(user_input)
    all_name_list.append(name_list)
    user_input = input("Enter a name (Enter to stop): ").title()

print("\n")
print("\033[91m========== ORIGINAL LIST OF NAMES ==========")

for a in all_name_list:
    print(a)

print("\033[97m\n")
ban = str(input("Select the letter you want removed: ")).upper()
print("\n")

filtered = []

for b in all_name_list:
    if b[0] != ban:
        filtered.append(b)

if all_name_list == filtered:
    print("No words were filtered.")

print("\033[94m========== FILTERED LIST OF NAMES ==========")
for c in filtered:
    print(c)
