class Question:
    def __init__(self,category, type, difficulty, question_text, question_answer, incorrect_answer):
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.text = question_text
        self.answer = question_answer
        self.incorrect_answer = incorrect_answer