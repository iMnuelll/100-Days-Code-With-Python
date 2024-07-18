def check_answer(guess, answer) :
    if guess == answer :
        return guess == guess
    else :
        return answer

def game() :
    answer = 4
    guess = int(input("2 + 2 = "))
    check_answer(guess, answer)
    if check_answer :
        print("Your answer is right!")
    else :
        print("Your answer is wrong!")
game()