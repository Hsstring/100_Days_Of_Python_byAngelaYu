def counter(attempt):
    attempt -=1
    return attempt

def guessing():
    guess = int(input("Make a guess: "))
    return guess

def eval(answer, guess):
    if answer == guess:
        print("Correct!")
        flag = True
    elif number> user_guess:
        print("Too low")
        print("Try again")
        flag = False
    else :
        print("Too high")
        print("Try again")
        flag = False
    return flag

import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(0,100)

if difficulty=="easy":
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        user_guess = guessing()
        result = eval(number, user_guess)
        if result:
            print("You Won!")
            break
        attempts-=1
    
    if attempts == 0:
        print(f"You lost! The number was {number}.")

elif difficulty=="hard":
    attempts = 5
    while attempts > 0:
        print(f"{attempts} attmepts remaining to guess the number.")
        user_guess = guessing()
        result = eval(number, user_guess)
        attempts-=1

    if attempts == 0:
        print(f"You lost! The number was {number}.")
else:
    print("Didn't catch that...")

#define the flag
#complete the evaluation function!