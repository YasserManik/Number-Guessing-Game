import random
def get_max_attempts():
    """Get the maximum number of attempts the user is allowed."""

    while True:
        try:
            max_attempts = int(input("How many guesses would you like? (Enter 'q' to quit) "))
            if max_attempts > 0:
                return max_attempts
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input, please enter a valid number.")

def get_range():
    """Get the range for the random number."""

    while True:
        try:
            low_num = int(input("Please enter the minimum number: "))
            high_num = int(input("Please enter the maximum number: "))
            if low_num < high_num:
                return low_num, high_num
            else:
                print("The minimum number must be less than the maximum number.")
        except ValueError:
            print("Invalid input, please enter valid numbers")

def get_guess(low_num, high_num):
    """Get the user's guess, ensuring that it is within the chosen range."""

    while True:
        guess = (input(f"Please enter a guess between {low_num} and {high_num} (or 'q' to quit): "))
        if guess == "q":
            return None
        if guess.isdigit():
            guess = int(guess)
            if low_num <= guess <= high_num:
                return guess
            else:
                print(f"That value is out of your chosen range, please enter a number between {low_num} and {high_num}: ")
        else:
                print("Invalid input, please enter a valid number")

def play_game():
    """Main game logic, including the guessing loop."""

    max_attempts = get_max_attempts()
    low_num, high_num = get_range()
    answer = random.randint(low_num, high_num)
    attempts = 0

    while attempts < max_attempts:
        print(f"Attempts remaining: {max_attempts - attempts}")
        guess = get_guess(low_num, high_num)

        if guess is None:
            print("You chose to quit. Thanks for playing!")
            return

        attempts += 1

        if guess < answer:
            print("Too low, try again.")
        elif guess > answer:
            print("Too high, try again.")
        else:
            print(f"CORRECT, the answer was {answer}")
            print(f"Number of guesses: {attempts}")
            break
    else:
        print(f"You have run out of guesses, the correct answer was: {answer}")

def main():
    """Entry point for the game with replay option."""

    while True:
        play_game()
        replay = input("Would you like to play again? y/n ").lower()
        if replay != "y":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()


















