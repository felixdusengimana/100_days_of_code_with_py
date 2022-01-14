from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(0, question_bank)

while quiz_brain.still_have_question():
    quiz_brain.next_question()

print("\n\n\n---------------------\nYou've completed the quiz.")
print(f"Your total score is {quiz_brain.score}/{quiz_brain.question_number}")