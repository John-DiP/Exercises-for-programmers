order_amount = int(input("What is the order amount? "))
state = input("What state do you live in? ").lower()

tax = 0

if state == "wisconsin":
    tax = order_amount * 0.05
    county = input("What county do you live in? ").lower()

    if county == "eau claire":
        tax += order_amount * 0.005
    elif county == "dunn":
        tax += order_amount * 0.004
    
    
elif state == "illinois":
    tax = order_amount * 0.08

total = order_amount + tax
print("The tax is $" + str(tax) + ".")
print("The total is $" + str(total) + ".")