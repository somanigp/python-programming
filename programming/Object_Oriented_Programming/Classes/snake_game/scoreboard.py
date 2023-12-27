from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # Write text with a Turtle object
        # Take this object to top, where we want it to write.
        self.penup()
        self.hideturtle()  # To hide the scoreboard (Turtle) object. It doesnt hide the writing
        self.goto(x=0, y=277)  # Go before and then write
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()  # remove what's written
        self.update_score()

    def game_over(self):
        # As not using clear here, we will still see latest score at top
        self.goto(x=0, y=0)  # Goto center and write
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


