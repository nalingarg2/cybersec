
print("Please enter the amount of money to convert:\n")

dollars = int(input("# of dollars: "))
cents = int(input("# of cents: "))

total = (dollars * 100) + cents
r = total

quaters = int(r / 25)
r = r % 25

dimes = int(r / 10)
r = r % 10

nickels = int(r / 5)
r = r % 5


print("The coins are {} quarters, {} dimes, {} nickels and {} pennies".format(quaters, dimes, nickels, r))
