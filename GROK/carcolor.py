import os

os.system('CLEAR')

car_colors = {}

while True:
    color = input("Car: ")
    if color == "":
        break
    if color in car_colors:
        car_colors[color] += 1
    else:
        car_colors[color] = 1

for color, count in car_colors.items():
    print(f"Cars that are {color}: {count}")
