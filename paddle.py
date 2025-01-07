from turtle import Turtle

PADDLE_WIDTH_MULT = 5
PADDLE_LENGTH_MULT = 1

MOVE_OFFSET = 20

class Paddle(Turtle):
    def __init__(self, spawn_location):
        super().__init__()
        self.create_paddle(spawn_location)

    def create_paddle(self, spawn_location):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(spawn_location)
        # to use forward instead of coordinates when calling move up/down
        # rotate the paddle 90 degrees, flip the width and length multipliers
        # and uncomment forward logic in move methods and comment out goto logic
        # self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_WIDTH_MULT, stretch_len=PADDLE_LENGTH_MULT, outline=None)

    def move_up(self):
        move_y = self.ycor() + MOVE_OFFSET
        # 340 - (length/2)
        # 340 - ((20 * 5)/2) = 290
        if self.ycor() <= 290:
            self.goto(x=self.xcor(), y=move_y)
            # self.forward(MOVE_OFFSET)

    def move_down(self):
        move_y = self.ycor() - MOVE_OFFSET
        if self.ycor() >= -290:
            self.goto(x=self.xcor(), y=move_y)
            # self.backward(MOVE_OFFSET)