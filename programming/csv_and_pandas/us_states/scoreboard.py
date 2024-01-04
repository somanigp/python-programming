class Scoreboard:
    def __init__(self):
        self.no_of_guesses = 0
        self.correct_guesses = 0
        self.total_guesses = 50

    def increase_guess(self):
        self.no_of_guesses += 1

    def increase_correct_guess(self):
        self.correct_guesses += 1

    def is_over(self):
        return self.no_of_guesses > 50
