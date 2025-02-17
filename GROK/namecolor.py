
namecolor = {}

nc = input("Name and color: ")

while nc:
    wndud = nc.split()
    name = wndud[0]
    color = wndud[1]

    namecolor[name] = color
    nc = input("Name and color: ")

# namecolor = {'a': '1', 'b': '2', 'c': '3'}

for name, color in namecolor.items():
    print(f"{name} {color}")
