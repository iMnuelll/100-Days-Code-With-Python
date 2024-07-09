from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data :
    question = Question(i.get('question'), i.get('correct_answer'))
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("This is the end of the QuizBrain")
print(f"Your final score is {quiz.current_score}/{quiz.question_number}")