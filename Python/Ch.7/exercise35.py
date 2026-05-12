import random

def main():
    names = []
    
    while True:
        name = input("Enter a name: ")

        if name == "":
            break
        
        names.append(name)

    winner = random.choice(names)

    print("The winner is... " + str(winner))

main()