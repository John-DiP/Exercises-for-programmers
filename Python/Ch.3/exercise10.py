price1 = int(input("Enter the price of item 1: "))
quantity1 = int(input("Enter the quantity of item 1: "))

price2 = int(input("Enter the price of item 2: "))
quantity2 = int(input("Enter the quantity of item 2: "))

price3 = int(input("Enter the price of item 3: "))
quantity3 = int(input("Enter the quantity of item 3: "))

item1 = price1 * quantity1
item2 = price2 * quantity2
item3 = price3 * quantity3

subtotal = item1 + item2 + item3

tax = subtotal * 0.055

total = subtotal + tax

print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(tax))
print("Total: $" + str(total))