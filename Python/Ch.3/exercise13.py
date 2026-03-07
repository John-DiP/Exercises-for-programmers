principal = int(input("What is the principal amount? "))
rateOfInterest = float(input("What is the rate? "))
years = int(input("What is the number of years? "))
compounded = int(input("What is the number of times the interest\nis compounded per year? "))

percentage = rateOfInterest / 100

amount = round(principal * (1 + (percentage / compounded)) ** (compounded * years), 2)

print("$" + str(principal) + " invested at " + str(rateOfInterest) + "% for " + str(years) + " years\n" + "compounded " + str(compounded) + " times per year is $" + str(amount) + ".")