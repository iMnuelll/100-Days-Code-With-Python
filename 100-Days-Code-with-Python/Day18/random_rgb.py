import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()

turtle.shape("turtle")
screen.colormode(255)

def random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r,g,b)
    return colours

degrees = [0, 90, 180, 270]

turtle.pensize(10)

for _ in range(100) :
    turtle.color(random_color())
    turtle.forward(40)
    turtle.setheading(random.choice(degrees))
    
screen.exitonclick()