from turtle import Turtle

BALL_SIZE_MULT = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=BALL_SIZE_MULT, stretch_len=BALL_SIZE_MULT)
        self.goto(x=0,y=0)
        self.setheading(0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(x=0, y=0)
        self.bounce_x()