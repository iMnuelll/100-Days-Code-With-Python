import random
from art import logo, vs
from game_data import data
import os

def get_random_account() :
    '''Get a random account'''
    return random.choice(data)

def format_data(account) :
    '''Format account into printable format: name, description, and country'''
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer (guess, a_follower, b_follower) :
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_follower > b_follower :
        return guess == "a"
    else :
        return guess == "b"
    
def game() :
    print(logo)
    games_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    score = 0
    while games_should_continue :
        account_a = account_b

        while account_a == account_b :
            account_b = get_random_account()
        print(f"Compare A: {format_data(account_a)}.")
        print(f"Compare B: {format_data(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system('cls||clear')
        print(logo)
        if is_correct :
            score += 1
            print(f"You are right! Current score: {score}\n")
        else :
            games_should_continue = False
            print(f" Sorry that's wrong! Final Score: {score}")
        
game()