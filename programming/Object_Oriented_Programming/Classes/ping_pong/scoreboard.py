from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.goto(0, 200)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_left} : {self.score_right}", move=False, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.score_left += 1
        self.clear()
        self.update_score()

    def increase_right_score(self):
        self.score_right += 1
        self.clear()
        self.update_score()
