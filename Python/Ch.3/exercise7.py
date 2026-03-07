length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))

print("You entered dimensions of " + str(length) + " feet " + "by " + str(width) + " feet. ")

resultInSquareFeet = length * width

resultInSquareMeters =  resultInSquareFeet * 0.09290304

print("The area is \n" + str(resultInSquareFeet) + " square feet \n" + str(resultInSquareMeters) + " square meters")

