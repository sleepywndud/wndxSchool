import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# clear()

print("\nPolynomial (Degree 2)\n")

while True:
    try:
        print("========================")

        a = float(input("\na : "))
        b = float(input("\nb : "))
        c = float(input("\nc : "))

        if a == 0:
            # IF a == 0, IT WOULD BE A LINEAR, NOT QUADRATIC.
            print("\nMa ERROR.\n")
            continue

        d = b**2 - 4*a*c  # DISCRIMINANT (** = ^)

        if d > 0:
            # '**0.5' = '√', AS POWER TO 1/2 (0.5) IS SQUARE ROOTING.
            x1 = (-b + d**0.5) / (2*a)
            x2 = (-b - d**0.5) / (2*a)
            print("\nTwo Real Solutions (D > 0):")
            print(f"    X1 [{x1}]")
            print(f"    X2 [{x2}]\n")
            
        elif d == 0:
            x = -b / (2*a)
            print("\nOne Real Solution (D = 0):")
            print(f"    X1 [{x}] × 2\n")
            
        else:
            print("\nNo Real Solution(s) (D < 0).\n")

    except ValueError:
        print("Invalid Input.\n")
