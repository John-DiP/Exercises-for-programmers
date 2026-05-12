import random

def main():

    question = input("What\'s your question? ")

    if len(question) > 0:
        responses = ["Yes", "No", "Maybe", "Ask again later."]
        response = random.choice(responses)
        print(response)
    else:
        print("A valid input is required")

main()