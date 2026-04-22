import random

def main():
    print("Let's play guess the number.")

    play_game_again = "y"

    while play_game_again == "y":

        difficulty = get_difficulty()

        if difficulty == 1:
            max_num = 10
        elif difficulty == 2:
            max_num = 100
        else:
            max_num = 1000

        secret = random.randint(1, max_num)
        play_game(secret)

        play_game_again = input("Play again? ").lower()
    
    print("Goodbye!")

def get_difficulty():
    while True:
        try:
            difficulty = input("Pick a difficulty level (1, 2, or 3): ")
            difficulty = int(difficulty)
            if difficulty > 0 and difficulty <= 3:
                return difficulty
            else:
                print("Select a valid difficulty level")
        except ValueError:
            print("A valid input is required")


def play_game(secret):
    
    guesses = int(input("I have my number. whats your guess? "))

    num_of_guesses = 1

    while True:
        
        if guesses < secret:
            guesses = int(input("Too low.   Guess again: "))
            num_of_guesses += 1
    
        elif guesses > secret:
            guesses = int(input("Too high.  Guess again: "))
            num_of_guesses += 1
    
        else:
            print("You go it in " + str(num_of_guesses) + " guesses! ")
            break
        
main()