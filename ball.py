from turtle import Turtle

BALL_SIZE_MULT = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=BALL_SIZE_MULT, stretch_len=BALL_SIZE_MULT)
        self.goto(x=0,y=0)
        self.setheading(0)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.xcor() + 10
        if self.ycor() <= 325:
            self.goto(new_x, new_y)