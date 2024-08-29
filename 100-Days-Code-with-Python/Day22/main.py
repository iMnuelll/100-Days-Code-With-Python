from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
right_paddle = Paddle(370, 0)
left_paddle = Paddle(-370, 0)
ball = Ball()

screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PING PONG")
screen.tracer(0)

screen.listen()
# Right paddle controller
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# Left paddle controller
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()
    
    # Detect collision with top or bottom wall
    if ball.ycor() > (SCREEN_HEIGHT / 2 - 20) or ball.ycor() < -(SCREEN_HEIGHT / 2 - 20):
        ball.bounce_y()
    
    # Detect collision with left or right wall
    if ball.xcor() > (SCREEN_WIDTH / 2) or ball.xcor() < -(SCREEN_WIDTH / 2):
        ball.bounce_x()
        
    
    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 :
        ball.bounce_x()
    
    # Detect collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340 :
        ball.bounce_x()


screen.exitonclick()