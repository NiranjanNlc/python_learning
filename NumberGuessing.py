import random

INDENT = " " * 40
LINE = "=" * 120

def ask_range():
    while True:
        top_number = input(INDENT + "Enter the maximum number for the guessing range: ")
        if top_number.isdigit():
            return int(top_number)
        else:
            print(INDENT + "Please enter a valid number only.")
            input(INDENT + "Press any key to try again.")

def check_guess(target_number, upper_limit):
    attempts = 0
    while True:
        attempts += 1
        user_input = input(INDENT + f"Guess a number between 0 and {upper_limit}: ")
        if user_input.isdigit():
            guess = int(user_input)
            if guess > target_number:
                print(INDENT + "Your guess is too high.")
            elif guess < target_number:
                print(INDENT + "Your guess is too low.")
            else:
                print(INDENT + "🎯 Correct! You've guessed it.")
                break
        else:
            print(INDENT + "Please enter a valid number.")
    return attempts

def main():
    print(" " * 20 + "🎮 Welcome to the Number Guessing Game 🎮")
    print(LINE)

    while True:
        upper_range = ask_range()
        target = random.randint(0, upper_range)
        attempts = check_guess(target, upper_range)

        print(LINE)
        print(INDENT + f"You guessed the number in {attempts} attempts.")

        user_input = input(INDENT + "Press 'q' to quit or any other key to play again: ")
        if user_input.lower() == 'q':
            break

if __name__ == '__main__':
    main()
