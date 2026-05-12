import statistics

def main():
    numbers = []
    
    while True:
        number = input("Enter a number: ")

        if number == "done":
            break
            
        numbers.append(int(number))
            
    average = statistics.mean(numbers)

    minimum = min(numbers)
    maximum = max(numbers)
    standard_deviation = statistics.stdev(numbers)
    standard_deviation = round(standard_deviation, 2)

    print("The average is " + str(average) + ".")
    print("The minimum is " + str(minimum) + ".")        
    print("The maximum is " + str(maximum) + ".")
    print("The standard deviation is " + str(standard_deviation) + ".")


main()