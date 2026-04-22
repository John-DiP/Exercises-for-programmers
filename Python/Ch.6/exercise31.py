def main():
    resting_heart_rate = int(input("What is your resting heart rate? "))
    age = int(input("What is your age? "))

    print("Intensity    | Rate  ")
    print("-------------|-------")

    for intensity in range(55, 100, 5):
        target_heart_rate = (((220 - age) - resting_heart_rate) * (intensity / 100)) + resting_heart_rate
        print(f"{intensity}%          | {round(target_heart_rate)} bpm")

main()