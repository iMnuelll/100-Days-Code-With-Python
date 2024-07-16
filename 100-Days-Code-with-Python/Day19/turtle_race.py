from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)

is_on = False

user_bet = screen.textinput(title="Guess a Turtle Color", prompt="Which turtle will win the race? Choose a color: red, green, blue, orange, yellow, black")
colors = ["red", "green", "blue", "orange", "yellow", "black"]
all_turtles = []

x_coordinate = -230
y_coordinate = -100

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=x_coordinate, y=y_coordinate)
    y_coordinate += 40
    all_turtles.append(new_turtle)

if user_bet :
    is_on = True
    
while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race.")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")
    
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()