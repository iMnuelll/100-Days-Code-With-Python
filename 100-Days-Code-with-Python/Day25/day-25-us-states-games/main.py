import turtle
import pandas as pd

"""Setup the screen"""
screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

"""Read the data"""
data = pd.read_csv("50_states.csv")

"""Make the series of the data into a list"""
state_list = data['state'].to_list()
x_cor = data['x'].to_list()
y_cor = data['y'].to_list()

"""Create a turtle for writing the state names"""
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()


def screen_answer():
    """The screen_answer function is designed to prompt the user to input a state name using a pop-up input box. 
    The prompt displays the number of correctly guessed states so far, out of the total number of states. 
    The user’s input is automatically converted to title case (i.e., capitalizing the first letter of each word). 
    The function then returns the user's input."""
    answer_state = screen.textinput(title=f"{len(guessed_states)} / {len(state_list)} States Correct", prompt="What's another state's name?").title()
    return answer_state

game_is_on = True

"""List of the correct states guess by the user"""
guessed_states = []

""""This while loop continuously prompts the user to guess U.S. state names until they have correctly guessed all 50 
states or choose to exit. The guessed states are tracked, and the state name is written at its corresponding geographic 
location on the screen if guessed correctly. If the player decides to exit by typing "Exit", the loop will terminate and 
save the list of unguessed states to a CSV file."""
while len(guessed_states) < 50:
    question = screen_answer()
    
    # If the player wants to exit, break the loop
    if question == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv", index=False)
        break
    
    if question in state_list and question not in guessed_states:
        guessed_states.append(question)  # Track guessed states
        state_index = state_list.index(question)
        
        # Get the coordinates for the guessed state
        x = x_cor[state_index]
        y = y_cor[state_index]
        
        # Write the state name at the correct position
        writer.goto(x, y)
        writer.write(question, align="center", font=("Arial", 6, "normal"))