from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward() :
    tim.forward(25)

def move_backward() :
    tim.backward(15)

def counter_clockwise() :
    tim.left(10)

def clockwise() :
    tim.right(10)
    
def clear_drawing() :
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forward, key="W")
screen.onkey(move_backward, key="S")
screen.onkey(counter_clockwise, key="A")
screen.onkey(clockwise, key="D")
screen.onkey(clear_drawing, key="C")

screen.exitonclick()