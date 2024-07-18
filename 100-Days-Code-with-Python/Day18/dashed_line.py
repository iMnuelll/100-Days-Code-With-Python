import turtle as t

turtle = t.Turtle()
screen = t.Screen()

turtle.shape("turtle")
for i in range (10) :
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    
screen.exitonclick()