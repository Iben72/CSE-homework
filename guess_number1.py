import random

def evaluate_performance(guess_count):
    if guess_count < 3:
        return "Excellent"
    elif guess_count < 5:
        return "Good"
    elif guess_count <= 6:
        return "Fair"
    else:
        return "Poor"

def play_game():
    secret_number = random.randint(1, 100)
    guess = -1
    guess_count = 0

    while guess != secret_number:
        try:
            guess = int(input("What is your guess? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guess_count += 1

        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:
            print("You got it!")

    print(f"It took you {guess_count} guesses.")
    print("Performance:", evaluate_performance(guess_count))

def main():
    keep_playing = "yes"
    while keep_playing.lower() == "yes":
        play_game()
        keep_playing = input("Would you like to play again? (yes/no): ")

if __name__ == "__main__":
    main()
