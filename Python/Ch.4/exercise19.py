weight = float(input("What is your weight in pounds? "))
height = float(input("What is your height in inches? "))

if weight < 0:
    weight = float(input("Please enter your weight in pounds and no negative numbers. "))
if height < 0:
    height = float(input("Please enter your height in inches and no negative numbers. "))

bmi = round((weight / (height * height)) * 703,1)

print("Your BMI is " + str(bmi) + ".")

if bmi >= 18.5 and bmi <= 25:
    print("You are within the ideal weight range.")
elif bmi < 18.5:
    print("You are underweight. You should see your doctor. ")
elif bmi > 25:
    print("You are overweight. You should see your doctor. ")