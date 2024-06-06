import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("Lower bound should be less than upper bound. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers. Try again.")

    while True:
        random_number = random.randint(lower_bound, upper_bound)
        attempts = 0

        while True:
            try:
                guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
                attempts += 1
                if guess < lower_bound or guess > upper_bound:
                    print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
                elif guess < random_number:
                    print("Too low! Try again.")
                elif guess > random_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number. Try again.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    start_game()
