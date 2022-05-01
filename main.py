from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []
for qn in question_data:
    qn_text = qn['text']
    qn_ans = qn['answer']
    new_qn = Question(qn_text, qn_ans)
    question_bank.append(new_qn)

quiz = QuizzBrain(question_bank)

while quiz.still_got_qn():
    quiz.next_qn()

print("You've completed the quizz")
print(f"Score: {quiz.score}/{quiz.question_no}")