from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizAppInterface:  # Pascal Case

    def __init__(self, quiz: QuizBrain):  # data_type of quiz is QuizBrain
        # NOTE: All the components are made as attributes so that they can be accessed anywhere in the class.
        # Setting window for Tk
        self.window = Tk()  # Window as an attribute gets executed when this class is initialized in that file.
        self.window.title("QuizzzApp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Getting the current quiz
        self.quiz = quiz

        # Score Text
        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "bold"))
        self.score_text.grid(row=1, column=2)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        # In text_board, width = 250 for wrapping text.
        self.text_board = self.canvas.create_text(150, 125,
                                                  width=250,  # Should be less than canvas width
                                                  text="Questions will be here",
                                                  fill=THEME_COLOR,
                                                  font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)  # For canvas add padding in grid.

        self.next_question()  # Printing-First Question

        # Buttons
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0,
                                  bg=THEME_COLOR, command=self.true_button_command)
        self.true_button.grid(row=3, column=1)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0,
                                   bg=THEME_COLOR, command=self.false_button_command)
        self.false_button.grid(row=3, column=2)

        # Mainloop: All the code after this mainloop will not be executed until this window is destroyed.
        self.window.mainloop()  # Like never ending while loop

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_text.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question: str = self.quiz.next_question()
            self.canvas.itemconfig(self.text_board, text=question)
        else:
            self.canvas.itemconfig(self.text_board, text="All Questions are done!! Thanks.")
            self.true_button.config(state="disabled")  # Disabling the button
            self.false_button.config(state="disabled")

    def true_button_command(self):
        check: bool = self.quiz.check_answer("true")
        self.give_feedback(check)

    def false_button_command(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self,check: bool):
        if check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
