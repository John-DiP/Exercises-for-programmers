print("Press C to convert from Fahrenheit to Celsius. ")
print("Press F to convert from Celsius to Fahrenheit. ")

formula = input("Your choice: ").lower()

print()

if formula == "c":
    temperature = float(input("Please enter the temperature in Fahrenheit: "))
    c = (temperature - 32) * (5/9)
    print("The temperature in Celsius is " + str(c) + ".")

elif formula == "f":
    temperature = float(input("Please enter the temperature in Celsius: "))
    f = (temperature * (9/5)) + 32
    print("The temperature in Fahrenheit is " + str(f) + ".")