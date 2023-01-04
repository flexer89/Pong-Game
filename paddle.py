from turtle import Turtle

MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.length = 6
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=self.length)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - MOVE_DISTANCE)

    def paddle_reset(self, position):
        self.goto(position)
