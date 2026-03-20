amount = int(input("What is the order amount? "))

state = input("What is the state? ")

if state == "WI":
    tax = amount * 0.055
    total = amount + tax
    print("The subtotal is $" + str(amount) + ".")
    print("The tax is $" + str(round(tax,2)) + ".")
    print("The total is $" + str(round(total,2)) + ".")
else:
    print("The total is $" + str(amount) + ".")