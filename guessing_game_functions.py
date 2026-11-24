# get_guess(): asks the player for number and returns it
# check_guess(guess, secret): returns "correct", "high", or "low"
# play_game(): runs the whole game using the two functions above
# then call play_game once at the bottom

import random

def get_guess():
    guess = int(input("Enter your guess: " ))
    return guess

def check_guess(guess,secret):
    if guess == secret:
        return "correct"
    elif guess > secret:
        return "high"
    else:
        return "low"

def play_again():
    answer = input("Play again? (yes/no): ")
    if answer.lower() == "yes":
        return True
    else:
        return False

def play_game():
    secret = random.randint(1,100)
    won = False
    attempts = 0
    while attempts < 7:
        guess = get_guess()
        attempts = attempts + 1
        result = check_guess(guess, secret)

        if result == "correct":
            print(f"You got it in {attempts} attempts")
            won = True
            break
        elif result == "high":
            print("Too high")
        else:
            print("Too low")
        print(f"guesses left {7 - attempts}")
    if not won:
        print(f"game over and the number was {secret}")

while True:
    play_game()  
    if not play_again():
        break



        
