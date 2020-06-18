import math

print("Please enter the number of coins:\n")

quarters = float(input("# of quarters: "))
dimes = float(input("# of dimes: "))
nickels = float(input("# of nickels: "))
pennies = float(input("# of pennies: "))

total = math.modf((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01))

dollar = int(total[1])
cent = int(total[0]*100)

print( "The total is {} dollars and {} cents".format(dollar, cent))
