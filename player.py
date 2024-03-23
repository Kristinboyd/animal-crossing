# Libraries
import time
from turtle import *
# Constants
from constants import *


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
