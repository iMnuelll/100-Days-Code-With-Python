import turtle as t
import random

turtle = t.Turtle()
screen = t.Screen()

screen.colormode(255)

def random_color() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r,g,b)
    return colours

def draw_spirograph (gap) :
    for _ in range (int(360 / gap)) :
        turtle.speed('fastest')
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap)
    
draw_spirograph(5)

screen.exitonclick()