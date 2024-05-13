from question_model import Question
from data import generation_question_data
from quiz_brain import QuizBrain
from ui import QuizAppInterface
import html

# https://www.w3schools.com/html/html_entities.asp
# NOTE: HTML Entities - Some characters are reserved in HTML. If you use the less than (<) or greater than (>)
# signs in your HTML text, the browser might mix them with tags.
# Entity names or entity numbers can be used to display reserved HTML characters.
# To display a less than sign (<) we must write: &lt; or &#60;

question_data: list = generation_question_data()
question_bank = []
for question in question_data:
    # https://stackoverflow.com/questions/2087370/decode-html-entities-in-python-string
    question_text = html.unescape(question["question"])  # html.unescape() to remove html Entities/Escapes or
    # unescapes an HTML file removing traces of offending characters that could be wrongfully interpreted as markup.
    # And convert to an intended text form.
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)  # Quiz is the main question/answer brain, an object of Quizbrain
quiz_app = QuizAppInterface(quiz)  # Passing the current quiz to QuizAppInterface

# while quiz.still_has_questions():  # A loop is already in quiz_app object, windows.mainloop and thus using
# this here will cause error, and confusion
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
