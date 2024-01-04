from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 8, 'normal')


class Name(Turtle):
    def __init__(self, name, x_cor, y_core):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.name = name
        self.xcor = x_cor
        self.ycor = y_core
        self.update()

    def update(self):
        self.goto(self.xcor, self.ycor)
        self.write(f"{self.name}", move=False, align=ALIGNMENT, font=FONT)


