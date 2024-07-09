from art import logo
import random

EASY_MODE_LIFE = 10
HARD_MODE_LIFE = 5

def answer_check(guess, answer, turns) :
    if guess > answer :
        print("Too high.")
        return turns - 1
    elif guess < answer :
        print("Too low.")
        return turns - 1
    else :
        print(f"You got it! The answer is {answer}.")

def set_difficulty() :
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy" :
        return EASY_MODE_LIFE
    elif level == "hard" :
        return HARD_MODE_LIFE

def game() :
    print(logo)
    print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100''')
    answer = random.randint(1, 100)
    print(f"Answer is {answer}.")

    turns = set_difficulty()
    
    guess = 0

    while guess!= answer :
        print(f"You have {turns} attempts remaining  to guess the number")
        guess = int(input("Make a guess: "))
        turns = answer_check(guess, answer, turns)
        if turns == 0 :
            print(f"You ran out of turns. The answer was {answer}")
            return
        elif guess != answer :
            print(f"Guess Again")
game()