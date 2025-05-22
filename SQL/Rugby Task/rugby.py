"""Program connecting SQLite (rugby) database and run queries (functions)."""

import sqlite3
from tabulate import tabulate
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def all_players():
    db = sqlite3.connect("Rugby.db")
    cr = db.cursor()

    all = cr.execute("""
        SELECT * 
        FROM player
        ;
    """).fetchall()

    headings = [
        "ID",
        "First Name",
        "Last Name",
        "Position",
        "Debut Year",
        "Test Caps",
        "Tries Scored",
        "Points Scored",
    ]
    alignments = [
        "left",
        "left",
        "left",
        "center",
        "center",
        "center",
        "center",
        "center",
    ]
    clear()

    print("Data of all players:\n")

    print(tabulate(all, headings, colalign=alignments))
    db.close()

def first_last_name():
    db = sqlite3.connect("Rugby.db")
    cr = db.cursor()

    all = cr.execute("""
        SELECT first_name, last_name
        FROM player
        WHERE position = "Fly-half"
        ;
    """).fetchall()

    headings = ["First Name", "Last Name"]
    alignments = ["left", "left"]

    clear()

    print("First & last Name of all fly-halfs:\n")

    print(tabulate(all, headings, colalign=alignments))
    db.close()

def most_point():
    db = sqlite3.connect("Rugby.db")
    cr = db.cursor()

    all = cr.execute("""
        SELECT first_name, last_name, debut_year
        FROM player
        WHERE points_scored = (SELECT MAX(points_scored) FROM player)
        ;
    """).fetchall()

    headings = ["First Name", "Last Name", "Debut Year"]
    alignments = ["left", "left"]

    clear()

    print("Player who has scored the most points:\n")

    print(tabulate(all, headings, colalign=alignments))
    db.close()

def fifty_tests():
    db = sqlite3.connect("Rugby.db")
    cr = db.cursor()
    
    all = cr.execute("""
        SELECT first_name, last_name
        FROM player
        WHERE debut_year > 2010
            AND test_caps > 50
        ;
    """).fetchall()

    headings = ["First Name", "Last Name"]
    alignments = ["left", "left"]

    clear()

    print(
        "Players who have started playing after 2010 who has more than 50 test caps:\n"
    )

    print(tabulate(all, headings, colalign=alignments))
    db.close()

clear()

print("\nWelcome! This program lets you query the All Blacks Database.")
print("Please choose a function from below:")

while True:
    try:
        userinput = input("""
1. Fetch Data of All Players
2. Fetch First & Last Names of All 'Fly-Half' Players
3. Fetch Player's First & Last Name who scored the most Points
4. Fetch player's first & last name who played more than 50 tests.\n\n\nEnter Function: """)
        
        if userinput == 1:
            all_players()
        elif userinput == 2:
            first_last_name()
        elif userinput == 3:
            most_point()
        elif userinput == 4:
            fifty_tests()
        elif userinput.lower() == "bobo":
            clear()
            print("Bye.")
            break
        else:
            clear()
            print("Invalid Input.")
            continue

    except ValueError:
        clear()
        print("Invalid Input.")