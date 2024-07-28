import numpy as np

def guessing():
    print("Guess the number between 1 and 100")
    print("Enter 0 to exit the program")
    n = np.random.randint(1,100)
    count =0
    while True:
        count += 1
        num = int(input("Enter your guess: "))
        if num == 0:
            print("Exiting the program...")
            break
        if n==num:
            print("Congratulations, you guessed the correct number!")
            print("Number of attempts taken: ", count)
            break
        elif num >n:
            print("Too high, guess a lower number.")
        else:
            print("Too low, guess a higher number.")

print("Welcome to the Number Guessing Game")
guessing()

choice = input("Do you want to play again? (y/n):")
if choice == "y":
    guessing()

