'''
A PROGRAM TO TEST PEOPLE/STUDENT'S MATH SKILLS.

CREATION DATE: 6TH OF APRIL 2025.
CREATED BY: WNDX2 (JAMES PARK).

CREATED FOR: PREPARATION FOR THE AS92004 SOFTWARE DEVELOPMENT EXAM.

'''

# NCEA AUTO does not support os import -- remove before submitting
import os
os.system('clear')

# list to hold all questions, options using nested lists, and the answer using dictionaries
# \n[033 stuffs are coloring the text, which increases visibility for the users
# spaces in "options" are to make differentiating (between Q, and Option) easier
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

# loops the whole thing in case the user wants to play again (see startornot userinput further below)
while True:
    try:
        # asks the user if they want to play the quiz
        startornot = str(input("Welcome to basic maths! Would you like to start the quiz? (Y/N): ")).strip().lower()
        if startornot == "y": # starting quiz
            score = 0 # initializing score
            for question in questions: 
                # printing questions and options
                print(question["question"])
                for option in question["options"]:
                    print(option)
                
                # loop to check if input is valid, and adds score depending on answer
                while True: 
                    try:
                        answer = str(input("\nType your answer: ")).strip().lower()
                        # checking if answer is valid (a,b,c,c)
                        if answer in ['a', 'b', 'c', 'd']:
                            # checking if answer is correct
                            if answer == question["answer"]:
                                print("\033[92mCorrect!\033[97m")
                                score += 1
                                break
                            else:
                                print("\033[91mIncorrect!\033[97m")
                                break
                        else:
                            # blocks any other inputs that are not a,b,c,d
                            print("Your answer is invalid, please try again.")

                    except ValueError: # blocks any other inputs that are not strings
                        print("Invalid Input. Please try again.")

            # score printing
            print(f"Your score is: {score}/6!")
            # asks if user wants to redo the test
            startornot = str(input("Want to redo the test? (Y/N) ")).strip().lower()
            if startornot == "y":
                # passing since the whole thing will loop again if not broke
                pass
            elif startornot == "n":
                # breaks if user input is n
                break
            else:
                # blocks any other inputs
                print("Please enter a vaild input.")

        # breaks straight away if user does not want to play (in starting question)
        elif startornot == "n":
            print("See you next time!")
            break
        
        # asks again if input is invalid in starting question
        else:
            print("Invalid input, please try again.")
    
    # blocks any other variable (input) types that are not strings
    except ValueError:
        print("Invald input, please try again.")
