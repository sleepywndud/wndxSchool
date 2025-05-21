"""Program connecting SQLite (rugby) database and run queries (functions)."""

import sqlite3
import tabulate
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

    print("Names:\n")

    print(tabulate(all, headings, colalign=alignments))
    db.close()


def first_last_name():
    all = cr.execute("""
        SELECT first_name, last_name
        FROM player
        WHERE position = "Fly-half"
        ;
    """).fetchall()

    headings = ["First Name", "Last Name"]
    alignments = ["left", "left"]

    print("First & last Name of all fly-halfs:\n")

    print(tabulate(all, headings, colalign=alignments))
    db.close()


def most_point():
    all = cr.execute("""
        SELECT first_name, last_name, debut_year
        FROM player
        WHERE points_scored = (SELECT MAX(points_scored) FROM player)
        ;
    """).fetchall()

    headings = ["First Name", "Last Name", "Debut Year"]
    alignments = ["left", "left"]

    print("Player who has scored the most points:\n")

    print(tabulate(all, headings, colalign=alignments))
    db.close()


def fifty_tests():
    all = cr.execute("""
        SELECT first_name, last_name
        FROM player
        WHERE debut_year > 2010
            AND test_caps > 50
        ;
    """).fetchall()

    headings = ["First Name", "Last Name"]
    alignments = ["left", "left"]

    print(
        "Players who have started playing after 2010 who has more than 50 test caps:\n"
    )

    print(tabulate(all, headings, colalign=alignments))
    db.close()


print("Welcome to a Python Program that searches the All Blacks Database!")
print("Please choose a function from below:")
fifty_tests()

