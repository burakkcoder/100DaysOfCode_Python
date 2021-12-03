class QuizBrain:
    def __init__(self,question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def has_questions(self):
        if self.q_number < len(self.q_list):
            return True
        return False

    def next_question(self):
        question = self.q_list[self.q_number]
        self.q_number += 1
        answer = input(f"Q.{self.q_number}: {question.text} (True/False): ")
        self.check(answer, question.answer)

    def check(self,answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score: {self.score}/{self.q_number}")
        print("\n")

