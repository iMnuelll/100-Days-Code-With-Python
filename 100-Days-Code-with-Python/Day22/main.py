from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

# Setup the screen
screen.title('PING PONG')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Setup the paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Setup the ball
ball = Ball()

# Setup the scoreboard
score_board = ScoreBoard()

screen.listen()

# Control the right paddle
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Control the left paddle
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with the paddles
    if ball.distance(r_paddle) < 30 and ball.xcor() > 330 or ball.distance(l_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x() 
    
    #Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.left_score()
    
    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.right_score()

screen.exitonclick()