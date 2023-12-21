class QuizBrain:
    # Methods are made in a way that they are able to work with Question Object.
    def __init__(self, question_list):  # Takes question_bank as input and creates a QuizBrain object
        self.question_number = 0  # to keep track of the question no. to show
        self.question_list = question_list
        self.score = 0  # to keep track of score on this object's quiz bank

    def new_question(self):  # Q.(0+1) - starts with 0.
        user_input = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True"
                           f"/False)?: ").lower()
        correct_answer = self.question_list[self.question_number].answer.lower()
        # self.question_list[self.question_number].text - how to access a list full of objects, self.question_number
        # tells which question this** object to show next.
        self.question_number += 1  # the question_number attribute for the object is increased so an object shows the
        # next question, next time.
        self.check_answer(user_input, correct_answer)  # How an object calls its own function
        print(f"Your current score is {self.score}/{self.question_number}")  # works as question_number already
        # increased by 1
        print("\n")  # Adding a new line to create scape between questions


    # still_has_question method checks if in the question_bank attribute, there is still questions left to show
    def still_has_questions(self):
        if (self.question_number + 1) == len(self.question_list):  # As question_number starts with 0( similar to index)
            # , Len of question_list will be question_number+1. Or the last index is len-1
            # Loop keeps going until the last index.
            return False  # returns boolean
        return True

    def check_answer(self, user_input, correct_input):
        if user_input == correct_input:
            self.score += 1  # Increase the object score by 1
            print("You got it Right!!")
        else:
            print("You got it Wrong!!")
        print(f"Correct answer is {correct_input}")
        # return user_input == correct_input # If same returns true or else will return false

