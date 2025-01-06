from turtle import Screen
import time
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("My Pong Game")
screen.tracer(0)

# Right paddle
r_paddle = Paddle(spawn_location=(350, 0))

# Left paddle
l_paddle = Paddle(spawn_location=(-350, 0))


screen.listen()
screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")
screen.onkey(l_paddle.move_up, key="w")
screen.onkey(l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0)




screen.exitonclick()