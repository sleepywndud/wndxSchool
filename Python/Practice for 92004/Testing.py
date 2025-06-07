'''TESTING PROGRAM IN PREPARATION FOR THE EXAM.'''

import os
# clearing terminal before running to provide cleaner output
os.system('clear')

# list of questions
questions = [
    {
        "question": "This is question one.",
        "options": ["1. Option One", "2. Option Two", "3. Option Three", "4. Option Four"],
        "answer": 1
    },
    {
        "question": "This is question two.",
        "options": ["1. Option One", "2. Option Two", "3. Option Three", "4. Option Four"],
        "answer": 2
    },
    {
        "question": "This is question three.",
        "options": ["1. Option One", "2. Option Two", "3. Option Three", "4. Option Four"],
        "answer": 3
    },
    {
        "question": "This is question four.",
        "options": ["1. Option One", "2. Option Two", "3. Option Three", "4. Option Four"],
        "answer": 4
    },
    {
        "question": "This is question five.",
        "options": ["1. Option One", "2. Option Two", "3. Option Three", "4. Option Four"],
        "answer": 5
    }
]

while True:
    score = 0
    try:
        start = str(input("Welcome! Would you like to start this super easy test? ")).strip().upper()
        if start == 'Y': # starting (expected)
            print("Starting 'Y'")
            for question in questions:
                # printing question
                print(question["question"])
                for option in question["options"]:
                    # printing options
                    print(option)
                
                while True:
                    try:
                        # taking answer
                        answer = int(input("Answer? "))
                        
                        # checking for expected cases
                        if answer in [1, 2, 3, 4]:
                            if answer == question['answer']:
                                print("Correct")
                                score += 1
                                break
                            else:
                                print("Incorrect")
                                break
                        else: # checking for boundary/invalid cases
                            print("Invalid input, try again.")

                    except ValueError: # output for boundary/invalid cases in answer input
                        print("ValueError")

            print("Ending")
            print(score,"/5")

        elif start == 'N': # not starting (expected)
            print("Breaking due to 'N' entered.")
            break

        else: # invalid/boundary exception for starting question
            print("Invalid input. Please enter either 'Y', or 'N',")    

    except ValueError: # invalid exception for starting question
        print("Invalid input. Please enter either 'Y', or 'N',")
