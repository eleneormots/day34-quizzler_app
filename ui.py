from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizzInteface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.click_on_true_button)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.click_on_false_button)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.get_text_question()
        self.window.mainloop()

    def get_text_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def response_on_click(self, is_correct:bool):
        if is_correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.response_on_click_end)

    def response_on_click_end(self):
            if self.quiz.question_number<10:
                self.canvas.config(bg="white")
                self.score_label.config(text=f"score: {self.quiz.score}")
                self.get_text_question()
            else:
                self.canvas.itemconfig(self.question_text, text=f"Your final score is :{self.quiz.score}")

    def click_on_true_button(self):
        is_correct=self.quiz.check_answer("true")
        self.response_on_click(is_correct)

    def click_on_false_button(self):
        is_correct=self.quiz.check_answer("false")
        self.response_on_click(is_correct)



