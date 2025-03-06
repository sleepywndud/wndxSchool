top_20_flavours = [
    "Vanilla", "Chocolate", "Boysenberry", "Hokey Pokey",
    "Mint Chocolate Chip", "Cookies & Cream", "Salted Caramel",
    "Mango", "Strawberry", "Pavlova", "Rum Raisin", 
    "Chocolate Chip", "Rocky Road", "Lemon Sorbet", "Macadamia Nut",
    "Coffee", "Peanut Butter", "Raspberry Ripple", "Green Tea",
    "Passionfruit"
]

icecream = str(input("What is your favourite ice cream? ")).title()
ic_pos = top_20_flavours.index(f"{icecream}")
counter = 0

if icecream in top_20_flavours:
    print(f"{icecream} is at position {ic_pos + 1} in the top 20 list.")
else:
    print("Your favourite flavour is too unique for this list!")

print(f"Top 20 ice cream flavours are: {", ".join(top_20_flavours)}")
