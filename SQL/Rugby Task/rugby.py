import sqlite3
import os

os.system("CLEAR")

db = sqlite3.connect("Rugby.db")
cr = db.cursor()

all = cr.execute("""
SELECT first_name, last_name, debut_year
                 FROM player
                 WHERE points_scored = (SELECT MAX(points_scored))  
""").fetchall()

for i in all:
    print(i)

# asdfasdf