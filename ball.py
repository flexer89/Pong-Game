import random
import time
from turtle import Turtle

ANGLES = [-17, -16, -15, -14, 14, 15, 16, 17]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.choice(ANGLES)
        self.y_move = random.randint(3, 6)
        self.move_speed = 0.03

    def move(self):
        time.sleep(self.move_speed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()



