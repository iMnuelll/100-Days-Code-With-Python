import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Car Racing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()
    
    car.create_car()
    car.move_cars()
    
    # Detect when the turtle cross the finish line
    if player.ycor() >= 300 :
        player.reset_turtle()
        scoreboard.update_score()
        car.speed_up()
    
    # Detect collisions with car
    for car_obj in car.all_cars:
        if car_obj.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()