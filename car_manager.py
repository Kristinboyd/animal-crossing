# Libraries
import random
# import time
from turtle import *
# Constants
from constants import *


class CarManager:

    def __init__(self):
        self.new_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=random.choice(CAR_LENGTH))
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_positions = random.randint(-250, 250)
            new_car.goto(x=320, y=y_positions)
            self.new_cars.append(new_car)

    def move_cars(self):
        for car in self.new_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
