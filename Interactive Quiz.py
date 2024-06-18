import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.user_answers = []
        self.correct_answers = []
        self.score = 0

    def start(self):
        print("Welcome to the Interactive Quiz!")
        print("You will be asked 100 questions. Try to answer them correctly.")
        
        for i, question in enumerate(self.questions):
            print(f"Question {i+1}: {question['question']}")
            user_answer = input("Your answer: ").strip()
            self.user_answers.append(user_answer)
            self.correct_answers.append(question['answer'])
            if user_answer == question['answer']:
                self.score += 1
        
        print("\nQuiz completed!")
        print(f"Your score: {self.score} out of {len(self.questions)}")
        self.review_answers()

    def review_answers(self):
        print("\nReview your answers:")
        for i in range(len(self.questions)):
            print(f"Question {i+1}: {self.questions[i]['question']}")
            print(f"Your answer: {self.user_answers[i]}")
            print(f"Correct answer: {self.correct_answers[i]}")
            print()

def generate_questions():
    questions = []
    operations = ['+', '-', '*', '/']
    for _ in range(100):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(operations)
        if operation == '+':
            question = f"What is {num1} + {num2}?"
            answer = str(num1 + num2)
        elif operation == '-':
            question = f"What is {num1} - {num2}?"
            answer = str(num1 - num2)
        elif operation == '*':
            question = f"What is {num1} * {num2}?"
            answer = str(num1 * num2)
        else:
            while num2 == 0:
                num2 = random.randint(1, 100)
            question = f"What is {num1} / {num2}?"
            answer = f"{num1 / num2:.2f}"
        questions.append({
            "question": question,
            "answer": answer
        })
    return questions

if __name__ == "__main__":
    questions = generate_questions()
    random.shuffle(questions)
    quiz = Quiz(questions)
    quiz.start()