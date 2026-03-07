euro = int(input("How many euros are you exchanging? "))
exchangeRate = float(input("What is the exchange rate? "))

usd = round((euro * exchangeRate) / 100, 2)

print(str(euro) + " euros at an exchange rate of " + str(exchangeRate) + " is\n" + str(usd) + " U.S. dollars ")