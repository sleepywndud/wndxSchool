# create a list of all the games owned
brothers_games = ["Lawnmowing Simulator", 
                  "Mario Kart 8", 
                  "Terraria", 
                  "Human: Fall Flat",
                  "Stardew Valley",
                  "Super Mario Bros. Wonder",
                  "Pikmin 4",
                  "Minecraft",
                  "Pokemon Violet"
]

# print out each game in the list 
for game in brothers_games:
  print(f"game: {game}")

# get input of a game and change it to title case
own_it = input("Check if I own this game: ").title()

# check if the input is in the game list and print the result
if own_it in brothers_games:
  print(f"You own {own_it}.")
else:
  print("Game not found.")
