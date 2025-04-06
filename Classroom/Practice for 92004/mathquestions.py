'''PREPARATION PROGRAM FOR THE AS92004 SOFTWARE EXAM'''

import os
os.system('clear')

# list to hold all questions, options using nested lists, and the answer using dictionaries
questions = [
    {
        "question": "\n\033[95m1 + 1 = \033[97m",
        "options": ["    a. 1", "    b. 2", "    c. 3", "    d. 4"],
        "answer": "b"
    },
    {
        "question": "\n\033[95m4 + 7 = \033[97m",
        "options": ["    a. 10", "    b. 15", "    c. 11", "    d. 16"],
        "answer": "c"
    },
    {
        "question": "\n\033[95m3 * 9 = \033[97m",
        "options": ["    a. 27", "    b. 12", "    c. -6", "    d. 3"],
        "answer": "a"
    },
    {
        "question": "\n\033[95m12 / 3 = \033[97m",
        "options": ["    a. 6", "    b. 9", "    c. 4", "    d. 8"],
        "answer": "c"
    },
    {
        "question": "\n\033[95m3^2 = \033[97m",
        "options": ["    a. 6", "    b. 32", "    c. 33", "    d. 9"],
        "answer": "d"
    },
    {
        "question": "\n\033[95mTRUE OR FALSE: \n9 / 0 = 0\033[97m",
        "options": ["    a. FaIse", "    b. False", "    c. Fal5e", "    d. Flase"],
        "answer": "b"
    },
]

while True:
    try:
        startornot = str(input("Welcome to basic maths! Would you like to start the quiz? (Y/N): ")).strip().lower()
        if startornot == "y":
            score = 0
            for question in questions:
                print(question["question"])
                for option in question["options"]:
                    print(option)
                
                while True: 
                    try:
                        answer = str(input("\nType your answer: ")).strip().lower()
                        if answer in ['a', 'b', 'c', 'd']:
                            if answer == question["answer"]:
                                print("\033[92mCorrect!\033[97m")
                                score += 1
                                break
                            else:
                                print("\033[91mIncorrect!\033[97m")
                                break
                        else:
                            print("Your answer is invalid, please try again.")

                    except ValueError:
                        print("Invalid Input. Please try again.")

            print(f"Your score is: {score}/6!")
            startornot = str(input("Want to redo the test? (Y/N) ")).strip().lower()
            if startornot == "y":
                pass
            elif startornot == "n":
                break
            else:
                print("Please enter a vaild input.")

        elif startornot == "n":
            print("Bye Bozo")
            break
        
        else:
            print("Invalid input, please try again.")

    except ValueError:
        print("Bye bozo")
        break
