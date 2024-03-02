from data import question_data
from qm import Question
from quizbrain import QuizBrain
from ui import QuizInterface

question_bank =[]
for i in question_data:
    question = Question(i['question'],i['correct_answer'])
    question_bank.append(question)

quizbrain = QuizBrain(question_bank)
quizui = QuizInterface(quizbrain)