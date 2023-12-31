from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_axis):
        super().__init__()
        self.shape("square")
        self.setheading(0)
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=x_axis, y=0)

    def move_up(self):
        # Heading is 0 that's why move right
        y_position = self.ycor()+20
        self.goto(x=self.xcor(), y=y_position)

    def move_down(self):
        y_position = self.ycor()-20
        self.goto(x=self.xcor(), y=y_position)

