car_silent = input("Is the car silent when you turn the key? ").lower()

if car_silent == "y":

    battery_corroded = input("Are the battery terminals corroded? ").lower()

    if battery_corroded == "y":
        print("Clean terminals and try starting again.")

    elif battery_corroded == "n":
        print("Replace cables and try again")

elif car_silent == "n":
    clicking_noise = input("Does the car make a clicking noise? ").lower()

    if clicking_noise == "y":
        print("Replace the battery.")

    elif clicking_noise == "n":
        fail_to_start = input("Does the car crank up but fail to start? ").lower()

        if fail_to_start == "y":
            print("Check spark plug connections.")

        elif fail_to_start == "n":
            engine = input("Does the engine start and then die? ").lower()

            if engine == "y":
                fuel_injection = input("Does your car have fuel injection? ").lower()

                if fuel_injection == "n":
                    print("Check to ensure the choke is opening and closing.")

                elif fuel_injection == "y":
                    print("Get it in for service.")
