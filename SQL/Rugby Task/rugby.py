import sqlite3
import os

os.system("CLEAR")

db = sqlite3.connect("Rugby.db")
cr = db.cursor()

def all_players():
    all = cr.execute("""
        SELECT * 
        FROM player
        ;
    """).fetchall()

    for client in all:
        print(client)
    db.close()

def first_last_name():
    all = cr.execute("""
        SELECT first_name, last_name
        FROM player
        WHERE position = "Fly-half"
        ;
    """).fetchall()

    for client in all:
        print(client[0], client[1])
    db.close()

def most_point():
    all = cr.execute("""
        SELECT first_name, last_name, debut_year
        FROM player
        WHERE points_scored = (SELECT MAX(points_scored) FROM player)
        ;
    """).fetchall()

    for client in all:
        print(f"{client[0]} {client[1]}, {client[2]}")
    db.close()

def fifty_tests():
    all = cr.execute("""
        SELECT first_name, last_name
        FROM player
        WHERE debut_year > 2010
            AND test_caps > 50
        ;
    """).fetchall()

    for client in all:
        print(f"{client[0]} {client[1]}")
    db.close()

