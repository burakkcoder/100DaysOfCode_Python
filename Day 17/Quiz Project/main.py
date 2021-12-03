from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for q in question_data:
    category = q["category"]
    type = q["type"]
    difficulty = q["difficulty"]
    question_text = q["question"]
    question_answer = q["correct_answer"]
    incorrect_answer = q["incorrect_answers"]
    new_question = Question(category, type, difficulty, question_text, question_answer, incorrect_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)

while quiz.has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score: {quiz.score}/{quiz.q_number}")