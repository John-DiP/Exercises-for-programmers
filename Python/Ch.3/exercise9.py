import math

length = int(input("Enter the length of the ceiling? "))
width = int(input("Enter the width of the ceiling? "))

COVERAGE_PER_GALLON = 350

area = length * width

result = math.ceil(area / COVERAGE_PER_GALLON)

print("You need to purchase " + str(result) + " gallons of \npaint to cover " + str(area) + " square feet.")
