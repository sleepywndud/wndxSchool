import sqlite3
import os

os.system("CLEAR")

db = sqlite3.connect("Rugby.db")
cr = db.cursor()

def all_players():
    all = cr.execute("""
        SELECT * FROM player
    """).fetchall()
    for client in all:
        print(client)
    
    db.close()

all_players()