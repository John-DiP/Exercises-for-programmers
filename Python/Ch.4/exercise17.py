weight = float(input("What is your weight? "))
gender = input("What is your gender? ")
number_of_drinks = int(input("What is the number of drinks? "))
alcohol_per_drink = float(input("What is the amount of alcohol by volume? "))
amount_of_time = float(input("What is the amount of time since your last drink? "))
                           
if weight < 0:
    weight = float(input("Weight cannot be negative. Enter again: "))

if number_of_drinks < 0:
    number_of_drinks = int(input("Number of drinks cannot be negative. Enter again: "))

if alcohol_per_drink < 0:
    alcohol_per_drink = float(input("Alcohol amount cannot be negative. Enter again: "))

if amount_of_time < 0:
    amount_of_time = float(input("Time cannot be negative. Enter again: "))


if gender == "male":
    r = 0.73
elif gender == "female":
    r = 0.66

A = number_of_drinks * alcohol_per_drink

bac = round((A * 5.14 / (weight * r)) - (0.015 * amount_of_time),4)

print("Your BAC is " + str(bac))

if bac >= 0.08:
    print("It is not legal for you to drive.")
else:
    print("It is legal for you to drive.")