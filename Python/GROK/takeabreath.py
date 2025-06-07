import os
os.system('clear')

best_time = 0
goal_time = 60
held_times = []
sorted_times = []

time = input('How long did you hold your breath? ')
time = int(time)
print(f"A personal best! {time} seconds is your best time.")
held_times.append(time)
held_times.sort(reverse=True)

while time != "":
    try:
        time = input('How long did you hold your breath? ')
        time = int(time)

        zero = held_times[0]

        # 33 AS A REC
        # ASSIGN ZERO AS PREVIOUS BIGGEST NUM
        if time > zero:
            print(f"A personal best! {time} seconds is your best time.")
        
        held_times.append(time)
        held_times.sort(reverse=True)

    except ValueError:
        break

print('Recording ended.')
print('Your results are:')
for t in held_times:
    print(f"{t} seconds")
