import sys

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number == second_number or first_number == third_number or second_number == third_number:
    print("Numbers must be different.")
    sys.exit()

largest_number = first_number 

if second_number > largest_number:
    largest_number = second_number

if third_number > largest_number:
    largest_number = third_number

print("The largest number " + str(largest_number) + ".")