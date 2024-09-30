from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer App-Awortwe")
        self.window.minsize(width=500, height=400)
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        self.scoreboard = Label(text=f"Scores:{self.quiz.score} ", width=20, bg=THEME_COLOR, fg="white", font=("Courier", 16, "normal"))
        self.scoreboard.grid(column=1, row=0)

        self.questionboard = Canvas(width=460, height=250, bg="white", highlightthickness=0)
        self.question_text = self.questionboard.create_text(230,
                                                            125,
                                                            width=440,
                                                            text="Wait patiently for your question",
                                                            fill=THEME_COLOR,
                                                            font=("Courier", 12, "normal"))
        self.questionboard.grid(column=0, row=1, columnspan=2)

        self.t_img = PhotoImage(file="images/true.png")
        self.t = Button(image=self.t_img, highlightthickness=0, bg=THEME_COLOR, command=self.true_answer)
        self.t.grid(column=0, row=4)

        self.f_img = PhotoImage(file="images/false.png")
        self.f = Button(image=self.f_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_answer)
        self.f.grid(column=1, row=4)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.questionboard.config(bg="white")
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            q_text = f"That's the end of the quiz\nYou had {self.quiz.score}/{self.quiz.question_number}"
            self.questionboard.itemconfig(self.question_text, text=q_text, font=("Courier", 24, "bold"))
            self.f.config(state="disabled")
            self.t.config(state="disabled")
        else:
            self.questionboard.itemconfig(self.question_text, text=q_text)

    def true_answer(self):
        user_answer = "True"
        self.get_feedback(self.quiz.check_answer(user_answer))
        self.scoreboard.config(text=f"Scores: {self.quiz.score}")

    def false_answer(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer)
        self.get_feedback(is_right)
        self.scoreboard.config(text=f"Scores: {self.quiz.score}")

    def get_feedback(self, is_right):
        if is_right:
            self.quiz.score += 1
            self.questionboard.config(bg="green")
        else:
            self.questionboard.config(bg="red")
        self.window.after(1000, self.get_next_question)
