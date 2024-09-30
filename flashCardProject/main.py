import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    learns = pd.DataFrame(to_learn)
    learns.to_csv("./data/words_to_learn.csv", index=False)

    next_card()


# -----------------------Creating UI-------------------
window = Tk()
window.title("Flash card Project")
# window.minsize(width=700, height=600)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_image)
card_title = canvas.create_text(400, 160, text="", font=("Courier", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Courier", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=6)

right_image = PhotoImage(file="./images/right.png")
btnCorrect = Button(image=right_image, highlightthickness=0, command=is_known)
btnCorrect.grid(column=4, row=1)

cross_image = PhotoImage(file="./images/wrong.png")
btnWrong = Button(image=cross_image, highlightthickness=0, command=next_card)
btnWrong.grid(column=1, row=1)

next_card()
window.mainloop()
