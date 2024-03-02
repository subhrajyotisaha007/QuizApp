from tkinter import *
from quizbrain import QuizBrain
THEME_COLOUR = '#375362'
YELLOW = '#f7f5dd'
WHITE = '#FFFFFF'
RED = '#e7305b'
GREEN = '#5FDF54'

class QuizInterface:
    def __init__(self,quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(pady=20,padx=20,bg=THEME_COLOUR)

        self.canvas = Canvas()
        self.canvas.config(width=400, height=400,bg=THEME_COLOUR,highlightthickness=0)
        img = PhotoImage(file='Images/small_dialogue.png')
        self.canvas.create_image(200,200,image= img)
        self.question_text = self.canvas.create_text(200, 200, text='HOLA', font=('Ariel', 15, 'italic'),width=200)
        self.canvas.grid(row=1,column=0,columnspan=2,sticky='EW',pady=20)


        #buttons
        self.true = Button()
        t_img = PhotoImage(file='Images/right_small.png')
        self.true.config(image=t_img,highlightthickness=0,command=self.True_ans)
        self.true.grid(row=2,column=0)

        self.false = Button()
        f_img = PhotoImage(file='Images/wrong_small.png')
        self.false.config(image=f_img,highlightthickness=0,command=self.False_ans)
        self.false.grid(row=2,column=1)

        #label
        self.score = Label()
        self.score.config(text='SCORE:',highlightthickness=0,bg=THEME_COLOUR,fg=WHITE,font=('Ariel',10,'bold'))
        self.score.grid(row=0,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=THEME_COLOUR)
        self.window.config(bg=THEME_COLOUR)
        self.score.config(bg=THEME_COLOUR)
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f'Game Over\nYour Score is : {self.quiz.score}')
            self.true.config(state='disabled')
            self.false.config(state='disabled')
        self.score.config(bg=THEME_COLOUR, text=f'SCORE:{self.quiz.score}')
    def True_ans(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def False_ans(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
            self.window.config(bg=GREEN)
            self.score.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
            self.window.config(bg=RED)
            self.score.config(bg=RED)
        self.window.after(1000, self.get_next_question)
