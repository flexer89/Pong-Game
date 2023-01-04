import random
import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

LEFT_PADDLE_POSITION = (-280, 0)
RIGHT_PADDLE_POSITION = (270, 0)
COLORS = ["#A93226", "#884EA0", "#2471A3", "#1ABC9C", "#229954", "#F1C40F", "#E67E22"]

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("background.gif")
screen.title("Pong game")
screen.tracer(0)

# Game options
end_score = int(input("How many points to win?"))
player_one_nick = input("Player one nickname: ")
player_two_nick = input("Player two nickname: ")
time.sleep(3)    # Starting delay

# Initialise objects and variables
game_is_on = True
scoreboard = Scoreboard(player_one_nick, player_two_nick)
left_paddle_color = random.choice(COLORS)
right_paddle_color = random.choice(COLORS)
left_paddle = Paddle(LEFT_PADDLE_POSITION, left_paddle_color)
right_paddle = Paddle(RIGHT_PADDLE_POSITION, right_paddle_color)
ball = Ball()

# Key pressing listener
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 250 or ball.distance(left_paddle) < 50 and ball.xcor() < -260:
        ball.bounce_x()

    # Detect Right paddle misses
    if ball.xcor() > 280:
        ball.reset_position()
        left_paddle.paddle_reset(LEFT_PADDLE_POSITION)
        right_paddle.paddle_reset(RIGHT_PADDLE_POSITION)
        scoreboard.l_point()

    # Detect Left paddle misses:
    if ball.xcor() < -290:
        ball.reset_position()
        left_paddle.paddle_reset(LEFT_PADDLE_POSITION)
        right_paddle.paddle_reset(RIGHT_PADDLE_POSITION)
        scoreboard.r_point()

    # Detect who win
    l_score = scoreboard.p1_score()
    r_score = scoreboard.p2_score()

    if end_score == l_score:
        scoreboard.finish(left_paddle_color, player_one_nick)
        time.sleep(3)
        exit(0)
    if end_score == r_score:
        scoreboard.finish(right_paddle_color, player_two_nick)
        time.sleep(3)
        exit(0)


screen.exitonclick()
