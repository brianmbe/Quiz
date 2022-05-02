from data import question_data, qn_type


class QuizzBrain:
    def __init__(self, qn_list):
        self.question_no = 0
        self.score = 0
        self.question_list = qn_list

    def still_got_qn(self):
        return self.question_no < len(self.question_list)

    def next_qn(self):
        current_qn = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f'Q.{self.question_no}: {current_qn.text} {qn_type[0]}: ')
        self.check_ans(user_answer, current_qn.answer)

    def check_ans(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('It is write')
        else:
            print(f"Correct answer is: {correct_answer}")
        print(f'The correct answer was: {correct_answer}')
        print(f"Your final score is : {self.score}/{self.question_no}")
        print('\n')
