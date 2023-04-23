from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

def choose_category():
    q_type = input("Choose a Category: Computers, Animals,or Random (C/A/R):").lower()
    test_data = []
    if q_type == 'c':
        test_data = [data for data in question_data if data['category'] == 'Science: Computers']
    elif q_type == 'a': 
        test_data = [data for data in question_data if data['category'] == 'Science: Animals']
    elif q_type == 'r':
        test_data = question_data
        random.shuffle(test_data)
    else:
        choose_category()
    return test_data[:10]

questions = choose_category()
question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
