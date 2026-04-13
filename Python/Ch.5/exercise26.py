import math

def main():
    balance = float(input("What is your balance? "))
    apr = float(input("What is the APR on the card (as a percent)? "))
    daily_rate = (apr / 100) / 365

    monthly_payment = float(input("What is the monthly payment you can make? "))

    number_of_months = calculateMonthsUntilPaidOff(balance, daily_rate, monthly_payment)

    print()
    print("It will take you " + str(number_of_months) + " months to pay off this card.")

def calculateMonthsUntilPaidOff(balance, daily_rate, monthly_payment):

    n = - (1 / 30) * math.log(1 + (balance / monthly_payment) * (1 - (1 + daily_rate) ** 30)) /  math.log(1 + daily_rate)

    return math.ceil(n)

main()