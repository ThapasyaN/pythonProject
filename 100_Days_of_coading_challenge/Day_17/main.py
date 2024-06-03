from question_model import Question
from Data import question_data
from quiz_brain import QuizzBrain
from quizz_brain_logo import logo

print(logo)
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizzBrain(question_bank)


while quizz.still_has_questions():
    quizz.next_question()

print("You have completed the quizz!")
print(f"Your' final score is: {quizz.score}/{quizz.question_number}")

