numOfPeople =int(input("How many People? "))
numOfPizzas = int(input("How many pizzas do you have? "))

print(str(numOfPeople) + " people with " + str(numOfPizzas) + " pizzas")

totalPizzas = numOfPizzas * 8

eachPerson = totalPizzas // numOfPeople

leftover = totalPizzas % numOfPeople

print("Each person gets " + str(eachPerson) + " pieces of pizza.")
print("There are " + str(leftover) + " leftover pieces.")