#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def take_quiz(self, quiz):
        print(f"Welcome to the {quiz.name} quiz!\n")
        for i, question in enumerate(quiz.questions, start=1):
            print(f"Question {i}: {question.text}")
            for choice_num, choice in enumerate(question.choices, start=1):
                print(f"{choice_num}. {choice}")
            user_choice = input("Your answer (enter the choice number): ")
            if user_choice == str(question.correct_choice):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        print(f"\nYour final score for the {quiz.name} quiz: {self.score}/{len(quiz.questions)}")

# Sample quiz data
python_quiz = Quiz("Python Basics", [
    Question("What is the capital of Brazil?", ["Sao Paulo", "Rio de Janeiro", "Brasilia"], 3),
    Question("Which of the following is NOT a Python data type?", ["Integer", "String", "Boolean"], 1),
    Question("What does the 'print' function do in Python?", ["Displays output", "Reads input", "Performs calculation"], 1)
])

# Sample user
user1 = User("John Doe")

# Take the Python quiz
user1.take_quiz(python_quiz)


# In[ ]:




