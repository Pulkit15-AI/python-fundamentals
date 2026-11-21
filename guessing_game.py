# import random and picks a secret number from 1 to 100
# start a loop that keep asking for guess
# if the guess is too low, say "too low"
# if the guess is too high, say "too high"
#if the guess is correct, say "you got it" and stop the loop

#----version:1---
# import random
# secret = random.randint(1,100)

# while True:
#     num = int(input("Enter your number: "))
#     if num == secret:
#         print("You got it")
#         break
#     elif num > secret :
#         print("too high")
        
#     else:
#         print("too low")


#----version:2---      
# import random

# secret = random.randint(1,100)
# attempts = 0

# while True:
#     guess = int(input("Enter your number: "))
#     attempts = attempts + 1

#     if guess == secret:
#         print(f"You got it in {attempts} attempts")

#         break
#     elif guess > secret :
#         print("too high")
        
#     else:
#         print("too low")

import random

secret = random.randint(1,100)
print(secret)
attempts = 0

while attempts < 7:
    guess = int(input("Enter your number: "))
    attempts = attempts + 1
    won = False

    if guess == secret:
        won = True 
        print(f"You got it in {attempts} attempts")

        break
    elif guess > secret :
        print("too high")
        print(f"guesses left = {7 - attempts} ")
        
    else:
        print("too low")
        print(f"guesses left = {7 - attempts} ")
if won == False:
    print(f"Game over, the number was {secret}")

      
    