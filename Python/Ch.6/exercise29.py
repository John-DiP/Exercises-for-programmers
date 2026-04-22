# Note: I was stuck on this for awhile so I had to ask ChatGPT to help me with the loop

def main():
    
    while True:
        try:
            rate_of_return = int(input("What is the rate of return? "))

            if rate_of_return == 0:
                print("Sorry that is not a valid input.")
            else:
                break

        except ValueError:
            print("Sorry that is not a valid input.")
            
    years = 72 / rate_of_return

    print("It will take " + str(years) + " years to double your investment")


main()