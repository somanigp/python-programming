from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction_of_x = 10
        self.direction_of_y = 10
        # Randomize initial pos

    def move_ball(self):
        x_position = self.xcor() + self.direction_of_x
        y_position = self.ycor() + self.direction_of_y
        self.goto(x=x_position, y=y_position)

    def bounce_on_wall(self):
        # Reverse a variable
        self.direction_of_y *= -1  # changing the direction on ball on y-axis.

    def bounce_on_paddle(self):
        self.direction_of_x *= -1

    def recenter(self):
        self.goto(0, 0)
