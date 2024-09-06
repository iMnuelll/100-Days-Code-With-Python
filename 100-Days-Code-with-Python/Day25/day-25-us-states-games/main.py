import turtle
import pandas as pd

# Setup the screen
screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# Read the data
data = pd.read_csv("50_states.csv")
state_list = data['state'].to_list()
x_cor = data['x'].to_list()
y_cor = data['y'].to_list()

# Create a turtle for writing the state names
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

def screen_answer():
    """Get the player's answer from the screen input."""
    answer_state = screen.textinput(title=f"{len(guessed_states)} / {len(state_list)} States Correct", prompt="What's another state's name?").title()
    return answer_state

game_is_on = True
guessed_states = []

while len(guessed_states) < 50:  # Game continues until all 50 states are guessed
    question = screen_answer()
    
    # If the player wants to exit, break the loop
    if question == "Exit":
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
    
    screen.update()

screen.exitonclick()