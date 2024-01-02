from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # As the program re-runs, all the objects are created again, and variables/attributes are initiated and given
        # values again.So some attributes like highscore which you want to retain, you need to store it in a database
        # or a text file. To remember a state you need a db to store values.
        with open("./data.txt") as data:  # By default, mode is read only
            self.highscore = int(data.read())  # Defining attribute here. Also .read() value is string here.
        # Write text with a Turtle object
        # Take this object to top, where we want it to write.
        self.penup()
        self.hideturtle()  # To hide the scoreboard (Turtle) object. It doesnt hide the writing
        self.goto(x=0, y=277)  # Go before and then write
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} Highscore : {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()  # remove what's written
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('./data.txt', mode="w") as data:
                # 'w' is 'write' access; it just overrides whatever already in the file.
                # 'a' is 'append' access; it adds to the already existing file.'\n' for newline there
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.update_score()

    def game_over(self):
        # As not using clear here, we will still see latest score at top
        self.goto(x=0, y=0)  # Goto center and write
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


