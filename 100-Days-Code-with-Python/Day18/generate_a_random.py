import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()

turtle.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
degrees = [0, 90, 180, 270 ]

turtle.pensize(10)

for _ in range(100) :
    turtle.color(random.choice(colours))
    turtle.forward(40)
    turtle.setheading(random.choice(degrees))
    
screen.exitonclick()