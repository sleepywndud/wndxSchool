
namecolour = {}

nc = input("Name and colour: ")

while nc:
    wndud = nc.split()
    name = wndud[0]
    colour = wndud[1]

    namecolour[name] = colour
    nc = input("Name and colour: ")

# namecolor = {'a': '1', 'b': '2', 'c': '3'}

for name, colour in namecolour.items():
    print(f"{name} {colour}")
