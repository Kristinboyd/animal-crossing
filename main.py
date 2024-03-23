# Libraries
import time
from turtle import Screen
# Classes
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
# Constants
# from constants import *

# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle Crossing")
screen.tracer(0)

# turtle player
player = Player()
# cars
car_manager = CarManager()
# scoreboard
scoreboard = Scoreboard()

# listeners
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.new_cars:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
