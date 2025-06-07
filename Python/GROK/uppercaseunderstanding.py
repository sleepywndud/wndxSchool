import os

if os.name == "nt":
    os.system("CLS")
else:
    os.system("CLEAR")

words = []
user_input = input("Sentence: ").split()
words.extend(user_input)
count = len(words)
capitals = 0

for i in words:
    if i == i.upper():
        capitals += 1

print(f"Number of words in capitals: {capitals}\n")
# print(words)
# print(count)
