import os

os.system('clear')

def debugging():
    print(passed)
    print(failed)

passed = []
failed = []

indexnum = 0

while True:
    try:
        score = input("Enter a test score (or type 'done' to finish): ")
        if score.lower() == 'done': 
            break
        score = int(score)
        if 0 <= score <= 100: 
            if score < 50:
                failed.append(score)
            elif score >= 50:
                passed.append(score)
        else: 
            print("Invalid input. Please enter a number between 0 and 100.")
    except ValueError: 
        print("Invalid input. Please enter an integer between 0 and 100.")

# output printing
print("Scores of students who passed:")
for wndud in passed:
    print(wndud)

print("Scores of students who failed:")
for wndud in failed: 
    print(wndud)

# nerdy maths
if len(passed) + len(failed) > 0:  
    numerator = sum(passed) + sum(failed)
    denominator = len(passed) + len(failed)
    average = round(numerator / denominator, 2)
    print(f"Average score: {average}")
else:
    # zero division error
    print("No scores were entered. Cannot calculate average.")
