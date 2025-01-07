from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("My Pong Game")
screen.tracer(0)

# Right paddle
r_paddle = Paddle(spawn_location=(350, 0))

# Left paddle
l_paddle = Paddle(spawn_location=(-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")
screen.onkey(l_paddle.move_up, key="w")
screen.onkey(l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce in y direction (of the wall)
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # needs to bounce in x direction (of the paddle)
        ball.bounce_x()

    # Detect right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()