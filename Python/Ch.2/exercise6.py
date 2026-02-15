from datetime import datetime

currentAge = input("What is your current age? ")
retirementAge = input("At what age would you like to retire? ")

int(currentAge)
int(retirementAge)

yearsToRetire = int(retirementAge) - int(currentAge)
currentYear = datetime.now().year
retirementYear = currentYear + yearsToRetire
print("You have " + str(yearsToRetire) + " years left until you can retire.")
print("It's " + str(currentYear) + ", so you can retire in " + str(retirementYear) + ".")