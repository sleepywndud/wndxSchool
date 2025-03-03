try:
  num_cookies = int(input("Cookies ordered for next week: "))
  if num_cookies < 0:
    print("Please enter the orders as a positive number")
  else:  
    flour = num_cookies * 10
    sugar = num_cookies * 5
    butter = num_cookies + 8
    choc_chips = num_cookies * 6
    print("We need to order:")
    print(f"{flour}g of flour")
    print(f"{sugar}g of sugar") 
    print(f"{butter}g of butter and")
    print(f"{choc_chips}g of chocolate chips next week.")
except ValueError:
  print("Did you enter a valid number?")
