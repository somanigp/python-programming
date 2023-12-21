from data import question_data, json_format_data
from question_model import Question
from quiz_brain import QuizBrain

# Managing JSON, which come through API
question_bank_for_json_format = []
list_of_json = json_format_data["results"]
for i in range(len(list_of_json)):
    question_bank_for_json_format.append(Question(list_of_json[i]["question"], list_of_json[i]["correct_answer"]))


# Doing this because question_data is how we generally get/transfer data through APIs, we are converting these data with
# a string key into objects and their attributes - more full proof way to access.
question_bank = []
for i in range(len(question_data)):  # question_data is a list.
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))  # Creating and Putting
    # Question objects in question_bank. Question objects need 2 inputs.

# print(question_bank[0].text) # question_bank[0] is an object of class Question

# quiz_brain = QuizBrain(question_bank_for_json_format)
quiz_brain = QuizBrain(question_bank)  # Creating a new QuizBrain Object. It has 2 attributes, one being a question_bank
# and other to track question_number

while quiz_brain.still_has_questions():
    quiz_brain.new_question()  # Need to call one method of an object, and it handles everything.

print("You have completed the quiz")
# Accessing 2 attributes of an object
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")  # len is last index + 1, and that was
# done in the last next_question method, so not needed now.

