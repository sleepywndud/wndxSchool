'''PROGRAM TO DETERMINE WHETHER IF A STUDENT HAS PASSED OR FAILED, AND CALCUALTE THE AVERAGE SCORE.'''

passed = []
failed = []

finish = 'done'
maxscore = 100
minscore = 0
half = 50

while True:
    try:
        score = input("Enter a test score (or type 'done' to finish): ")
        if score.lower() == finish: 
            # CHECKING IF INPUT IS DONE BEFORE ANYTHING ELSE.
            break 
        score = int(score) # CHANGING VARIABLE TYPE TO INTEGER.
        if minscore <= score <= maxscore: 
            # APPENDING SCORE AS YOU TYPE.
            if score < half:
                failed.append(score) 
            elif score >= half:
                passed.append(score)
        else: 
            # BOUNDARY CHECKNING FOR BELOW 0 AND OVER 100.
            print("Invalid input. Please enter a number between 0 and 100.")
    except ValueError: # INVALID CHECKING FOR OTHER VARIABLE TYPES (STR, FLOAT, COMPLEX, ETC..)
        print("Invalid input. Please enter an integer between 0 and 100.")

# OUTPUT PRINTING.
print("Scores of students who passed:")
for wndud in passed:
    print(wndud)

print("Scores of students who failed:")
for wndud in failed: 
    print(wndud)

# MATHS.
if len(passed) + len(failed) > 0:  
    # SETTING NUMERATORS AND DENOMINATORS.
    numerator = sum(passed) + sum(failed)
    denominator = len(passed) + len(failed)
    average = round(numerator / denominator, 2)
    # CALCUALTING AVERAGE.
    print(f"Average score: {average}")
else:
    # ZERO DIVISION / UNABLE TO CALCULATE ERROR.
    print("No scores were entered. Cannot calculate average.")
