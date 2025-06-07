price = int(input("Price of computer: "))
monthly_amount = int(input("Amount of pocket money: "))

# Initialise counter to keep track of the number of months
count = 0

# Initialise the current_savings to the monthly amount of pocket money 
current_savings = monthly_amount

if current_savings >= price:
  print("You have enough money to buy the computer now!")
else:
  while price > current_savings:
    current_savings += monthly_amount
    interest = 0.05 * current_savings  
    current_savings += interest 
    count = count + 1
  print(f"It will take {count} months to buy the computer.")
