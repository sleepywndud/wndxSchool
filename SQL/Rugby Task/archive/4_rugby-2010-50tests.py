import sqlite3
import os

os.system("CLEAR")

db = sqlite3.connect("Rugby.db")
cr = db.cursor()

all = cr.execute("""
    SELECT first_name, last_name
    FROM player
    WHERE debut_year > 2010
        AND test_caps > 50
""").fetchall()

for i in all:
    print(i)