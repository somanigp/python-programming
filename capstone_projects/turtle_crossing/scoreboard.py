from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#76453B")
        self.goto(x=-290, y=240)
        self.level = 1
        self.write_score()

    def write_score(self):
        self.write(f"LEVEL : {self.level}", move=False, align='left', font=FONT)

    def increase_sore(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(x=0, y=0)  # Method clear not used, thus score doesn't disappear.
        self.write(f"GAME OVER!!", move=False, align='center', font=FONT)

