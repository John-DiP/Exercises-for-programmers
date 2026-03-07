principal = int(input("Enter the principal: "))
rateOfInterest = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))

simpleInterest = round(principal * (1 + rateOfInterest/100 * years), 2)

print("After " + str(years) + " years at " + str(rateOfInterest) +"%, the investment will\n" + " be worth $" + str(simpleInterest) + ".")