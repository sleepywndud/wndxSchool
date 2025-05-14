import sqlite3
import os

os.system("CLEAR")

db = sqlite3.connect("Rugby.db")
cr = db.cursor()

all = cr.execute("SELECT * FROM player;").fetchall()

for i in all:
   print(i)