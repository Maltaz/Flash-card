import random
import pandas

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

#---------------------- Read data from csv -------------------#
try:
    data = pandas.read_csv("D:/Flash_card/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")



def random_word():
    """Docstring"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    window.after(3000, func=translate_word)


def translate_word():
    """Docstring"""
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(title_txt, fill="white", text="English")
    canvas.itemconfig(word_txt, fill="white", text=current_card["English"])


def is_known():
    """Docstring"""
    word_dict.remove(current_card)
    datap = pandas.DataFrame(word_dict)
    datap.to_csv("data/words_to_learn.csv", index=False)
    random_word()

#---------------------- UI Setup -----------------------------#


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=translate_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="D:/Flash_card/images/card_front.png")
back_card = PhotoImage(file="D:/Flash_card/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)

title_txt = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#x_button
wrong = PhotoImage(file="D:/Flash_card/images/wrong.png")
button_x = Button(image=wrong, highlightthickness=0, command=random_word)
button_x.grid(row=1, column=0)

#v_button
right = PhotoImage(file="D:/Flash_card/images/right.png")
button_v = Button(image=right, highlightthickness=0, command=is_known)
button_v.grid(row=1, column=1)


window.mainloop()

