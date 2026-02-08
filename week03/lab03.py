import random

def generate_mad_lib(adjective, noun, verb):
    story = f"In a world of magic, a {adjective} {noun} suddenly {verb} into the scene, surprising everyone around."
    return story

def guessing_game():
    
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != secret_number:
        user_input = input("Enter your guess: ")
        guess = int(user_input)
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")


if __name__ == '__main__':
    guessing_game()